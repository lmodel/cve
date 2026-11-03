"""Checks the fetch of the pinned CVE records against stubbed downloads.

scripts/fetch_cve_records.py downloads each record the manifest pins and keeps it
only when its size and both hashes match. These tests replace its opener with a
stub, so they run offline. They show that a matching download is kept, that a wrong,
oversized or cut-off one is not, and that the script refuses an address or a redirect
off raw.githubusercontent.com and a name that leaves the destination.
"""

import hashlib
import http.client
import importlib.util
import io
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "fetch_cve_records.py"
GOOD = b'{"dataType": "CVE_RECORD"}\n'
NAME = "cves/1900/1xxx/CVE-1900-1234.json"


@pytest.fixture
def fetch():
    spec = importlib.util.spec_from_file_location("fetch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _manifest(data=GOOD, name=NAME):
    return {
        "repository": "CVEProject/cvelistV5",
        "commit": "a" * 40,
        "fetched": {
            name: {
                "size": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
                "git_blob": hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest(),
            }
        },
    }


def _serve(fetch, monkeypatch, body):
    """Answer every request with `body`, and list the addresses asked."""
    asked = []

    def opener(req, timeout):
        asked.append(req.full_url)
        return body() if callable(body) else io.BytesIO(body)

    monkeypatch.setattr(fetch, "_open", opener)
    return asked


def test_a_matching_download_is_kept(fetch, monkeypatch, tmp_path):
    """A download with the pinned size and hashes lands at its place."""
    asked = _serve(fetch, monkeypatch, GOOD)
    assert not fetch.fetch(tmp_path, _manifest())
    assert (tmp_path / NAME).read_bytes() == GOOD
    assert asked == [
        f"https://raw.githubusercontent.com/CVEProject/cvelistV5/{'a' * 40}/{NAME}"
    ]
    assert not list(tmp_path.rglob("*.part"))


def test_a_record_already_present_is_not_downloaded(fetch, monkeypatch, tmp_path):
    """A copy that matches its pins needs no request."""
    (tmp_path / NAME).parent.mkdir(parents=True)
    (tmp_path / NAME).write_bytes(GOOD)
    asked = _serve(fetch, monkeypatch, b"never read")
    assert not fetch.fetch(tmp_path, _manifest())
    assert asked == []


def test_a_wrong_copy_is_replaced(fetch, monkeypatch, tmp_path):
    """A copy that does not match its pins is downloaded again."""
    (tmp_path / NAME).parent.mkdir(parents=True)
    (tmp_path / NAME).write_bytes(b"something else")
    _serve(fetch, monkeypatch, GOOD)
    assert not fetch.fetch(tmp_path, _manifest())
    assert (tmp_path / NAME).read_bytes() == GOOD


@pytest.mark.parametrize(
    "body",
    [b'{"dataType": "CVE_RECORD!"}\n', GOOD + b"more", GOOD[:5]],
    ids=["other bytes", "oversized", "short"],
)
def test_a_mismatch_is_not_kept(fetch, monkeypatch, tmp_path, body):
    """A download of another size or hash leaves nothing behind and reports."""
    _serve(fetch, monkeypatch, body)
    problems = fetch.fetch(tmp_path, _manifest())
    assert problems == [
        f"{NAME}: the download does not match its pinned size and hashes"
    ]
    assert not (tmp_path / NAME).exists()


def test_an_oversized_answer_is_not_read_whole(fetch, monkeypatch):
    """The read stops one byte past the pinned size."""

    class Answer(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    _serve(fetch, monkeypatch, lambda: Answer(b"x" * 1000))
    assert len(fetch._download("https://raw.githubusercontent.com/a", 10)) == 11


@pytest.mark.parametrize(
    "failure",
    [
        urllib.error.URLError("Connection refused"),
        urllib.error.HTTPError("https://x", 404, "Not Found", None, None),
        http.client.IncompleteRead(b"", 1),
        ValueError("a redirect off the host"),
    ],
    ids=["refused", "404", "cut off", "redirect"],
)
def test_a_failed_download_is_reported(fetch, monkeypatch, tmp_path, failure):
    """A failure stops one record, says so and writes nothing."""

    def body():
        raise failure

    _serve(fetch, monkeypatch, body)
    problems = fetch.fetch(tmp_path, _manifest())
    assert len(problems) == 1 and problems[0].startswith(f"{NAME}: the download failed")
    assert not (tmp_path / NAME).exists()


def test_a_name_that_leaves_the_destination_is_refused(fetch, monkeypatch, tmp_path):
    """A path in the manifest cannot climb out of the destination."""
    asked = _serve(fetch, monkeypatch, GOOD)
    problems = fetch.fetch(tmp_path / "dest", _manifest(name="../outside.json"))
    assert len(problems) == 1 and "would be written outside" in problems[0]
    assert asked == []
    assert not (tmp_path / "outside.json").exists()


@pytest.mark.parametrize(
    "url",
    [
        "http://raw.githubusercontent.com/a",
        "https://example.org/a",
        "https://raw.githubusercontent.com.example.org/a",
    ],
)
def test_an_address_off_the_host_is_refused(fetch, url):
    with pytest.raises(ValueError, match="is not an https address"):
        fetch._check_address(url)


def test_a_redirect_off_the_host_is_refused(fetch):
    """A redirect is followed over https on the pinned host, and nowhere else."""
    handlers = fetch._open.__self__.handlers
    assert any(isinstance(h, fetch._PinnedHostRedirect) for h in handlers)
    handler = fetch._PinnedHostRedirect()
    req = urllib.request.Request("https://raw.githubusercontent.com/a")
    with pytest.raises(ValueError, match="is not an https address"):
        handler.redirect_request(req, None, 302, "Found", {}, "https://example.org/a")
    moved = "https://raw.githubusercontent.com/b"
    assert (
        handler.redirect_request(req, None, 301, "Moved", {}, moved).full_url == moved
    )


def test_the_manifest_names_only_paths_in_the_list(fetch):
    """Every pinned record is a CVE record's file under cves/, at a full commit."""
    import json

    manifest = json.loads(fetch.MANIFEST.read_text(encoding="utf-8"))
    assert len(manifest["commit"]) == 40
    assert manifest["repository"] == "CVEProject/cvelistV5"
    for name in manifest["fetched"]:
        assert name.startswith("cves/") and name.endswith(".json"), name
        assert ".." not in name, name

"""Checks the upstream watch's decisions against stubbed answers.

scripts/check_upstream_release.py asks the GitHub API about the CVE Program's
repositories. These tests replace its one network call, `_get`, with a table
of answers, so they run offline. They show what the report says in each case
the watch knows: a new release, a moved tag, a changed, dropped or added file,
a changed licence, changed terms, and a check that could not finish.
"""

import http.client
import importlib.util
import json
import urllib.error
from pathlib import Path

import pytest

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check_upstream_release.py"


@pytest.fixture
def watch():
    """A fresh copy of the script, so no test sees another's stub."""
    spec = importlib.util.spec_from_file_location("watch_under_test", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _tree(files):
    return {
        "truncated": False,
        "tree": [{"path": p, "type": "blob", "sha": s} for p, s in files.items()],
    }


def _not_found(url):
    return urllib.error.HTTPError(url, 404, "Not Found", None, None)


def _answers(watch, tag_files=None, head_files=None):
    """The answers of an unchanged upstream, with the parts a test changes."""
    tag_files = dict(watch.PINNED_BLOBS) if tag_files is None else tag_files
    head_files = dict(watch.PINNED_BLOBS) if head_files is None else head_files
    terms = f"{watch.WEBSITE_API}/contents/{watch.TERMS_PATH}?ref=dev"
    return {
        f"{watch.SCHEMA_API}/releases/latest": {"tag_name": watch.PINNED_TAG},
        f"{watch.SCHEMA_API}/commits/{watch.PINNED_TAG}": {"sha": watch.PINNED_COMMIT},
        f"{watch.SCHEMA_API}/git/trees/{watch.PINNED_TAG}?recursive=1": _tree(
            tag_files
        ),
        watch.SCHEMA_API: {"default_branch": "main"},
        f"{watch.SCHEMA_API}/git/trees/main?recursive=1": _tree(head_files),
        f"{watch.SCHEMA_API}/license": {"license": {"spdx_id": watch.PINNED_LICENCE}},
        f"{watch.RECORDS_API}/license": _not_found(f"{watch.RECORDS_API}/license"),
        watch.WEBSITE_API: {"default_branch": "dev"},
        terms: {"sha": watch.PINNED_TERMS_BLOB},
    }


def _stub(watch, answers):
    """Make `_get` answer from the table: an exception is raised, bytes are
    returned as they are, and anything else is JSON."""

    def get(url):
        answer = answers[url]
        if isinstance(answer, Exception):
            raise answer
        if isinstance(answer, bytes):
            return answer
        return json.dumps(answer).encode()

    watch._get = get


def _run(watch, tmp_path):
    report = tmp_path / "report.md"
    code = watch.main(["--report", str(report)])
    return code, report.read_text(encoding="utf-8")


def test_nothing_changed(watch, tmp_path):
    """With the pinned edition, files, licences and terms, the watch exits 0."""
    _stub(watch, _answers(watch))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert "The latest release is the pinned edition, v5.2.0." in text
    assert "The tag v5.2.0 is at the pinned commit." in text
    assert f"holds all {len(watch.PINNED_BLOBS)} pinned files." in text
    assert "`main` leaves the pinned files as they are." in text
    assert "names CC0-1.0, as pinned." in text
    assert "states no licence, as pinned." in text
    assert "The source of the Terms of Use is the pinned file." in text


def test_a_newer_release(watch, tmp_path):
    """A latest release other than the pin needs attention."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/releases/latest"] = {"tag_name": "v5.3.0"}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The latest release is `v5.3.0`; the schema renders v5.2.0.**" in text


def test_a_moved_tag(watch, tmp_path):
    """A tag at another commit needs attention."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/commits/{watch.PINNED_TAG}"] = {"sha": "1" * 40}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The tag v5.2.0 is now at commit `111111111111`" in text


def test_the_tag_lost_a_file(watch, tmp_path):
    """A pinned file with another blob at the tag needs attention."""
    files = dict(watch.PINNED_BLOBS, **{"schema/tags/cna-tags.json": "b" * 40})
    _stub(watch, _answers(watch, tag_files=files))
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "no longer holds `schema/tags/cna-tags.json` as the pinned blob" in text


def test_a_change_on_the_default_branch_is_for_information(watch, tmp_path):
    """The default branch moves ahead of releases, so a changed file, a dropped
    one and a new one beside them are reported and leave the exit code at 0."""
    files = dict(watch.PINNED_BLOBS, **{"schema/tags/cna-tags.json": "b" * 40})
    del files["schema/tags/adp-tags.json"]
    files["schema/imports/cvss/cvss-v5.0.json"] = "c" * 40
    _stub(watch, _answers(watch, head_files=files))
    code, text = _run(watch, tmp_path)
    assert code == 0, text
    assert (
        "`main` has changed or dropped `schema/tags/adp-tags.json`, "
        "`schema/tags/cna-tags.json` since the pinned tag." in text
    )
    assert "also holds `schema/imports/cvss/cvss-v5.0.json`" in text


def test_another_licence(watch, tmp_path):
    """Another licence on the format's repository needs attention."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/license"] = {"license": {"spdx_id": "MIT"}}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The format's repository now names `MIT`, not CC0-1.0.**" in text


def test_no_licence_on_the_format(watch, tmp_path):
    """No licence on the format's repository needs attention too."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/license"] = {"license": None}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "now names `None`, not CC0-1.0" in text


def test_the_record_list_states_a_licence(watch, tmp_path):
    """A licence the record list comes to state needs attention."""
    answers = _answers(watch)
    answers[f"{watch.RECORDS_API}/license"] = {"license": {"spdx_id": "CC-BY-4.0"}}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The record list's repository now states a licence, `CC-BY-4.0`.**" in text


def test_the_terms_changed(watch, tmp_path):
    """Another blob for the Terms of Use source needs attention."""
    answers = _answers(watch)
    terms = f"{watch.WEBSITE_API}/contents/{watch.TERMS_PATH}?ref=dev"
    answers[terms] = {"sha": "d" * 40}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The Terms of Use changed:" in text
    assert "is blob `dddddddddddd`" in text


def test_the_terms_are_gone(watch, tmp_path):
    """A Terms of Use source that has moved needs attention, not a crash."""
    answers = _answers(watch)
    terms = f"{watch.WEBSITE_API}/contents/{watch.TERMS_PATH}?ref=dev"
    answers[terms] = _not_found(terms)
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**`{watch.TERMS_PATH}` is gone from `dev`.**" in text


@pytest.mark.parametrize(
    ("failure", "shown"),
    [
        (
            urllib.error.HTTPError("https://x", 403, "Forbidden", None, None),
            "`HTTP Error 403",
        ),
        (urllib.error.URLError("Connection refused"), "`<urlopen error"),
        (http.client.IncompleteRead(b"{"), "`IncompleteRead"),
        (EOFError("cut"), "`cut`"),
        (LookupError("unknown encoding: x-bogus"), "`unknown encoding"),
        (
            ValueError("the answer is larger than 5000000 bytes"),
            "`the answer is larger",
        ),
    ],
)
def test_a_check_that_could_not_finish(watch, tmp_path, failure, shown):
    """A refused, failed, cut-off or oversized answer stops one check, says so,
    and leaves the other checks to run and the report to be written."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/releases/latest"] = failure
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert f"**The release check could not finish: {shown}" in text
    assert "states no licence, as pinned" in text


def test_json_of_another_shape_could_not_finish(watch, tmp_path):
    """An API answer without the keys the watch reads is a check that could not
    finish, not a crash."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/releases/latest"] = {"message": "moved"}
    answers[f"{watch.SCHEMA_API}/license"] = {"license": "not an object"}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The release check could not finish: `'tag_name'`.**" in text
    assert "**The licences check could not finish: `" in text


def test_a_json_list_where_an_object_belongs_could_not_finish(watch, tmp_path):
    """An API answer that is a list, where the watch reads an object's key,
    raises a TypeError, which is a check that could not finish."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/releases/latest"] = b'["v5.2.0"]'
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The release check could not finish: `list indices" in text


def test_a_truncated_tree_could_not_finish(watch, tmp_path):
    """A file listing GitHub cut short cannot show the pinned files are there."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/git/trees/{watch.PINNED_TAG}?recursive=1"] = {
        "truncated": True,
        "tree": [],
    }
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "**The files check could not finish: `the tree at v5.2.0" in text


def test_text_the_server_chose_is_quoted_on_one_line(watch, tmp_path):
    """A tag name with a blank line, a mention and a backtick stays inside its
    code span, so the issue mentions no one."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/releases/latest"] = {"tag_name": "v9\n\n@someone `x`"}
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert "The latest release is `v9 @someone 'x'`;" in text


class _Answer:
    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False

    def read(self, size):
        return b"{}"


def test_the_token_travels_in_an_unredirected_header(watch, monkeypatch):
    """The token goes to api.github.com in a header urllib does not copy onto a
    redirect, and a request to any other host carries no token."""
    monkeypatch.setenv("GITHUB_TOKEN", "not-to-leak")
    sent = {}

    def urlopen(req, timeout):
        sent[req.full_url] = (dict(req.header_items()), dict(req.unredirected_hdrs))
        return _Answer()

    monkeypatch.setattr(watch, "_open", urlopen)
    watch._get(watch.SCHEMA_API)
    watch._get("https://example.org/elsewhere")
    headers, unredirected = sent[watch.SCHEMA_API]
    assert unredirected["Authorization"] == "Bearer not-to-leak"
    assert headers["User-agent"] == "lmodel-cve-watch"
    other, other_unredirected = sent["https://example.org/elsewhere"]
    assert "Authorization" not in other and not other_unredirected


def test_an_answer_over_the_cap_is_refused(watch, monkeypatch):
    """An answer larger than MAX_BYTES raises rather than being read whole."""

    class Big(_Answer):
        def read(self, size):
            return b"x" * size

    monkeypatch.setattr(watch, "_open", lambda req, timeout: Big())
    with pytest.raises(ValueError, match="larger than"):
        watch._get(watch.SCHEMA_API)


def test_a_redirect_off_the_expected_host_is_refused(watch):
    """A redirect is followed over https to the GitHub API, and nowhere else."""
    handlers = watch._open.__self__.handlers
    assert any(isinstance(h, watch._ExpectedHostRedirect) for h in handlers)
    handler = watch._ExpectedHostRedirect()
    req = watch.urllib.request.Request(watch.SCHEMA_API)
    for newurl in (
        "https://example.org/repos/CVEProject/cve-schema",
        "http://api.github.com/repos/CVEProject/cve-schema",
        "https://api.github.com.example.org/repos/CVEProject/cve-schema",
        "https://raw.githubusercontent.com/CVEProject/cve-schema/main/README.md",
    ):
        with pytest.raises(ValueError, match="leads off the expected hosts"):
            handler.redirect_request(req, None, 302, "Found", {}, newurl)
    moved = "https://api.github.com/repositories/1/license"
    assert (
        handler.redirect_request(req, None, 301, "Moved", {}, moved).full_url == moved
    )


def test_a_refused_redirect_could_not_finish(watch, tmp_path):
    """A redirect the watch refuses stops that check, and the report quotes the
    address it was sent to."""
    answers = _answers(watch)
    answers[f"{watch.SCHEMA_API}/license"] = ValueError(
        "a redirect leads off the expected hosts, to https://example.org/@someone"
    )
    _stub(watch, answers)
    code, text = _run(watch, tmp_path)
    assert code == 1
    assert (
        "**The licences check could not finish: `a redirect leads off the expected "
        "hosts, to https://example.org/@someone`.**" in text
    )

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Fetch the pinned sample of real CVE records into tmp/ and check each one.

tests/data/cvelist/manifest.json pins a varied sample of the CVE list: each
record's path at one commit of CVEProject/cvelistV5, its size, its SHA-256 and its
git object hash. The list is too large to keep in git, so this script downloads
the sample instead. For each record it:

- keeps a copy already in the destination when its size and both hashes match;
- otherwise downloads it to a temporary file beside its place, stopping at the
  pinned size, and moves it into place only when the size and both hashes match;
- deletes a download that does not match, and exits 1 once every record has been
  tried.

It builds each address from the manifest alone. It refuses an address, or a
redirect to one, that is not https on raw.githubusercontent.com. It writes nothing
outside the destination, which is tmp/cvelist/ unless --dest names another folder.
Usage::

    python scripts/fetch_cve_records.py [--dest DIR]
"""

from __future__ import annotations

import argparse
import hashlib
import http.client
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "tests" / "data" / "cvelist" / "manifest.json"
DEST = ROOT / "tmp" / "cvelist"
HOST = "raw.githubusercontent.com"
USER_AGENT = "lmodel-cve-fetch"
CHUNK = 1 << 20


def _hashes(data: bytes) -> tuple[int, str, str]:
    """The byte count, SHA-256 and git object hash of a record."""
    return (
        len(data),
        hashlib.sha256(data).hexdigest(),
        hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest(),
    )


def _matches(data: bytes, pin: dict) -> bool:
    return _hashes(data) == (pin["size"], pin["sha256"], pin["git_blob"])


def _target(dest: Path, name: str) -> Path:
    """Where a record goes, refusing a name that would leave the destination."""
    target = (dest / name).resolve()
    if not target.is_relative_to(dest.resolve()):
        raise ValueError(f"{name} would be written outside {dest}")
    return target


def _check_address(url: str) -> None:
    """Refuse an address that is not https on the pinned host."""
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname != HOST:
        raise ValueError(f"{url} is not an https address on {HOST}")


class _PinnedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on the pinned host."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        _check_address(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener without the default redirect handler, which follows a redirect to
# any address.
_open = urllib.request.build_opener(_PinnedHostRedirect).open


def address(manifest: dict, name: str) -> str:
    """A record's address at the pinned commit."""
    path = urllib.parse.quote(name)
    return f"https://{HOST}/{manifest['repository']}/{manifest['commit']}/{path}"


def _download(url: str, size: int) -> bytes:
    """Download an address, stopping one byte past the pinned size so that an
    oversized answer fails the check without filling the memory."""
    _check_address(url)
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with _open(req, timeout=120) as resp:
        return resp.read(size + 1)


def fetch(dest: Path, manifest: dict) -> list[str]:
    """Fetch every pinned record that the destination lacks, and return a line for
    each problem."""
    problems = []
    kept = downloaded = 0
    for name, pin in sorted(manifest["fetched"].items()):
        try:
            target = _target(dest, name)
        except ValueError as err:
            problems.append(str(err))
            continue
        if target.is_file() and _matches(target.read_bytes(), pin):
            kept += 1
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            data = _download(address(manifest, name), pin["size"])
        # OSError covers a refused or failed request and a timeout,
        # HTTPException a download cut off mid-read, and ValueError an address
        # or a redirect off the pinned host.
        except (OSError, http.client.HTTPException, ValueError) as err:
            problems.append(f"{name}: the download failed: {err}")
            continue
        if not _matches(data, pin):
            problems.append(
                f"{name}: the download does not match its pinned size and hashes"
            )
            continue
        part = target.with_name(target.name + ".part")
        # A file left at the temporary name, even a link, is replaced, not
        # written through.
        part.unlink(missing_ok=True)
        part.write_bytes(data)
        os.replace(part, target)
        downloaded += 1
    print(f"{kept} records already present, {downloaded} downloaded")
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEST,
        help="Folder to fetch into, by default tmp/cvelist/",
    )
    args = parser.parse_args(argv)
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    problems = fetch(args.dest, manifest)
    for line in problems:
        print(line, file=sys.stderr)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///
"""Check the CVE Program's repositories against the edition the schema renders.

The schema renders the CVE Record Format at the tag pinned below, and upstream/
holds that tag's files unchanged. Real records come from a second repository
and are used under the Terms of Use, whose text lives in a third. Five things
can change without any change in this repository:

- the CVE Program releases another edition of the format;
- the pinned tag moves, or stops holding a pinned file;
- the format's repository changes its licence;
- the record list's repository states a licence, where it states none today;
- the Terms of Use change.

The script asks the GitHub API about all three repositories and compares files
by git object hash, so it downloads nothing but listings. The website's page
of the Terms is written by script, so the watch reads its source file.

It prints a Markdown report, and exits 1 when:

- the latest release is another edition;
- the pinned tag is at another commit;
- the pinned tag no longer holds a pinned file as its pinned blob;
- the format's repository names another licence, or none;
- the record list's repository states a licence;
- the Terms of Use source changed or is gone;
- a check could not finish, such as a refused, failed or cut-off request, or
  an answer larger than the script reads.

A pinned file that the default branch has changed or dropped, and a new file
beside the schema's own, are reported for information only: the format's
default branch moves ahead of its releases, and the release check is what asks
for a person.

Text a server chose, such as a tag, a file name or an error message, is quoted
as code on one line in the report, so the issue the workflow opens from it
cannot mention anyone. A redirect is followed only to an https address on
api.github.com. Set ``GITHUB_TOKEN`` to raise the API rate limit. The token goes
to api.github.com alone, in a header that is not copied onto a redirect. Usage::

    python scripts/check_upstream_release.py [--report FILE]
"""

from __future__ import annotations

import argparse
import http.client
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from functools import cache
from pathlib import Path

USER_AGENT = "lmodel-cve-watch"
API_HOST = "https://api.github.com/"
# The one host a redirect may lead to.
HOSTS = frozenset({"api.github.com"})
SCHEMA_API = f"{API_HOST}repos/CVEProject/cve-schema"
RECORDS_API = f"{API_HOST}repos/CVEProject/cvelistV5"
WEBSITE_API = f"{API_HOST}repos/CVEProject/cve-website"

# The most the script reads of one answer. The largest, the format's file tree,
# is about 20 kB.
MAX_BYTES = 5_000_000

# The edition the schema renders, its canonical address, and the commit its tag
# is at. tests/test_upstream.py holds the schema header and these pins equal.
# Move them together, with upstream/ and the header, for another edition.
PINNED_EDITION = "5.2.0"
PINNED_TAG = "v5.2.0"
PINNED_COMMIT = "5533f6038cc0434e544e69240c704906d591de46"
PINNED_SOURCE = (
    "https://github.com/CVEProject/cve-schema/blob/v5.2.0/schema/CVE_Record_Format.json"
)
PINNED_LICENCE = "CC0-1.0"

# Each file upstream/ holds, by its path in the format's repository, with its
# git object hash. tests/test_upstream.py holds upstream/ to this list.
PINNED_BLOBS = {
    "LICENSE.txt": "0e259d42c996742e9e3cba14c677129b2c1b6311",
    "schema/CVE_Record_Format.json": "223e94b7fb38632b4ea46ae00d479221c4096f5f",
    "schema/docs/cnaContainer-advanced-example.json": "a5091d79d063abed5094d84285601a99a147e426",
    "schema/docs/cnaContainer-basic-example.json": "04ca59c65fd9a6716dc6cfc48466798372504503",
    "schema/docs/cnaContainer-rejected-example.json": "e9d0f9fc4790787a3ee6b3753b7d4a49ba780009",
    "schema/docs/full-record-advanced-example.json": "c49bd0d82c327603954170ced0b9658cf94cbd2b",
    "schema/docs/full-record-basic-example.json": "5f9425c18179b86996bcf211e44f8c413a511cb7",
    "schema/imports/cvss/README.md": "174dd1658af8e7afbea8b360931c1bfc87f5e6b7",
    "schema/imports/cvss/cvss-v2.0.json": "caa64037aab6d6feffae1a25929c7c27f13714dd",
    "schema/imports/cvss/cvss-v3.0.json": "fceaf5f825d9e4118e0fecf423d863f6c24445ab",
    "schema/imports/cvss/cvss-v3.1.json": "89fcd20cb846bb3f94a0610cc2c26b2603423922",
    "schema/imports/cvss/cvss-v4.0.json": "262616b03254bd418b30bb760c5081a8fa805249",
    "schema/tags/adp-tags.json": "d16868a91bd1a0d860591b821abdf9fad4d6d101",
    "schema/tags/cna-tags.json": "35633c72ecb96b90023d9ef4d777345eb7958741",
    "schema/tags/reference-tags.json": "41a1aebe7af081e0037976a4c1c53923fe15ae12",
}

# The folders whose new files are worth a reader's look: another imported
# scoring system or another tag list would change what the schema must render.
WATCHED = ("schema/imports/cvss/", "schema/tags/")

# The Terms of Use source in the website's repository, and its git object hash.
TERMS_PATH = "src/views/Legal/TermsOfUse.vue"
PINNED_TERMS_BLOB = "5502b4275d4cf30f9d616dcd01a462e86adfa6f6"


class _ExpectedHostRedirect(urllib.request.HTTPRedirectHandler):
    """Follow a redirect only to an https address on one of HOSTS."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        parts = urllib.parse.urlsplit(newurl)
        if parts.scheme != "https" or parts.hostname not in HOSTS:
            raise ValueError(f"a redirect leads off the expected hosts, to {newurl}")
        return super().redirect_request(req, fp, code, msg, headers, newurl)


# An opener in place of urlopen's, whose redirect handler follows any address.
_open = urllib.request.build_opener(_ExpectedHostRedirect).open


def _get(url: str) -> bytes:
    """The body of an answer from the GitHub API, read up to the cap."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    }
    req = urllib.request.Request(url, headers=headers)
    token = os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API_HOST):
        # urllib copies ordinary headers onto a redirect, so the token goes in
        # an unredirected one and reaches api.github.com alone.
        req.add_unredirected_header("Authorization", f"Bearer {token}")
    with _open(req, timeout=60) as resp:
        body = resp.read(MAX_BYTES + 1)
    if len(body) > MAX_BYTES:
        raise ValueError(f"the answer from {url} is larger than {MAX_BYTES} bytes")
    return body


def _json(url: str):
    return json.loads(_get(url))


def _code(text: object) -> str:
    """Text a server chose, as a code span on one line, so it cannot mention a
    person or add a link in the issue. A blank line would end the span, so
    every run of spaces and line breaks is one space."""
    return "`" + " ".join(str(text).replace("`", "'").split()) + "`"


@cache
def _tree(ref: str) -> dict[str, str]:
    """Every file of the format's repository at a ref, by path, with its object
    hash. A ref the repository does not hold gives an empty mapping. Each tree
    is asked for once, and no caller changes what it returns."""
    try:
        body = _json(f"{SCHEMA_API}/git/trees/{ref}?recursive=1")
    except urllib.error.HTTPError as err:
        if err.code in (404, 422):
            return {}
        raise
    if body.get("truncated"):
        raise OSError(f"the tree at {ref} is too large for one listing")
    return {e["path"]: e["sha"] for e in body.get("tree", []) if e["type"] == "blob"}


def check_release() -> tuple[list[str], bool]:
    """Report whether the latest release is the pinned edition and whether the
    pinned tag is still at the pinned commit."""
    report, attention = [], False
    latest = _json(f"{SCHEMA_API}/releases/latest")["tag_name"]
    if latest != PINNED_TAG:
        attention = True
        report.append(
            f"- **The latest release is {_code(latest)}; the schema renders "
            f"{PINNED_TAG}.** Read what changed, decide whether the schema moves to "
            "it, and move upstream/, the pins here and the schema headers together."
        )
    else:
        report.append(f"- The latest release is the pinned edition, {PINNED_TAG}.")
    commit = _json(f"{SCHEMA_API}/commits/{PINNED_TAG}")["sha"]
    if commit != PINNED_COMMIT:
        attention = True
        report.append(
            f"- **The tag {PINNED_TAG} is now at commit {_code(commit[:12])}, not "
            f"`{PINNED_COMMIT[:12]}`.** Find out why it moved before trusting the copy."
        )
    else:
        report.append(f"- The tag {PINNED_TAG} is at the pinned commit.")
    return report, attention


def check_files() -> tuple[list[str], bool]:
    """Report whether the pinned tag holds every pinned file, and what the
    default branch has done to them since."""
    report, attention = [], False
    pinned_tree = _tree(PINNED_TAG)
    for name, sha in sorted(PINNED_BLOBS.items()):
        if pinned_tree.get(name) != sha:
            attention = True
            report.append(
                f"- **The tag {PINNED_TAG} no longer holds `{name}` as the pinned "
                "blob.** Find out what happened before trusting the copy in upstream/."
            )
    if not attention:
        report.append(
            f"- The tag {PINNED_TAG} holds all {len(PINNED_BLOBS)} pinned files."
        )

    branch = _json(SCHEMA_API)["default_branch"]
    head = _tree(branch)
    moved = sorted(n for n, sha in PINNED_BLOBS.items() if head.get(n) != sha)
    if moved:
        report.append(
            f"- For information, {_code(branch)} has changed or dropped "
            + ", ".join(_code(n) for n in moved)
            + " since the pinned tag. A release would ask for a person."
        )
    added = sorted(
        path for path in head if path.startswith(WATCHED) and path not in PINNED_BLOBS
    )
    if added:
        report.append(
            f"- For information, {_code(branch)} also holds "
            + ", ".join(_code(n) for n in added)
            + " beside the files the schema renders."
        )
    if not moved and not added:
        report.append(f"- {_code(branch)} leaves the pinned files as they are.")
    return report, attention


def check_licences() -> tuple[list[str], bool]:
    """Report whether the format's repository still names the pinned licence,
    and whether the record list still states none. GitHub answers 404, or names
    no licence, when it detects none."""
    report, attention = [], False
    found = (_json(f"{SCHEMA_API}/license").get("license") or {}).get("spdx_id")
    if found != PINNED_LICENCE:
        attention = True
        report.append(
            f"- **The format's repository now names {_code(found)}, not "
            f"{PINNED_LICENCE}.** Read what it allows and update NOTICE and upstream/."
        )
    else:
        report.append(f"- The format's repository names {PINNED_LICENCE}, as pinned.")
    try:
        records = (_json(f"{RECORDS_API}/license").get("license") or {}).get("spdx_id")
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        records = None
    if records:
        attention = True
        report.append(
            f"- **The record list's repository now states a licence, {_code(records)}.** "
            "Read what it allows beside the Terms of Use, and update NOTICE."
        )
    else:
        report.append("- The record list's repository states no licence, as pinned.")
    return report, attention


def check_terms() -> tuple[list[str], bool]:
    """Report whether the source of the Terms of Use is the pinned file."""
    branch = _json(WEBSITE_API)["default_branch"]
    url = f"{WEBSITE_API}/contents/{TERMS_PATH}?ref={urllib.parse.quote(branch)}"
    try:
        sha = _json(url)["sha"]
    except urllib.error.HTTPError as err:
        if err.code != 404:
            raise
        return [
            f"- **`{TERMS_PATH}` is gone from {_code(branch)}.** Find where the Terms "
            "of Use now live, read them, and update NOTICE and the pin."
        ], True
    if sha != PINNED_TERMS_BLOB:
        return [
            f"- **The Terms of Use changed: `{TERMS_PATH}` on {_code(branch)} is blob "
            f"{_code(sha[:12])}.** Read what changed, update NOTICE and "
            "tests/data/cvelist/TERMS.txt if the licence moved, and move the pin."
        ], True
    return ["- The source of the Terms of Use is the pinned file."], False


# Each check, by the name the report gives it when it cannot finish.
CHECKS = (
    ("release", check_release),
    ("files", check_files),
    ("licences", check_licences),
    ("terms of use", check_terms),
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--report", type=Path, help="Also write the Markdown report to this file"
    )
    args = parser.parse_args(argv)
    lines = [
        f"- Pinned edition: the CVE Record Format {PINNED_EDITION}, {PINNED_SOURCE}."
    ]
    attention = False
    for label, check in CHECKS:
        try:
            found, needs = check()
        # OSError covers a refused or failed request and a timeout,
        # HTTPException and EOFError a connection cut off mid-answer,
        # ValueError an answer that is not JSON or is too large, and
        # LookupError, TypeError and AttributeError JSON of another shape.
        except (
            OSError,
            http.client.HTTPException,
            EOFError,
            ValueError,
            LookupError,
            TypeError,
            AttributeError,
        ) as err:
            found = [f"- **The {label} check could not finish: {_code(err)}.**"]
            needs = True
        lines += found
        attention = attention or needs
    text = "\n".join(lines) + "\n"
    print(text, end="")
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    return 1 if attention else 0


if __name__ == "__main__":
    sys.exit(main())

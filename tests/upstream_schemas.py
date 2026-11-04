"""The upstream's own JSON schemas, as validators the tests can compare with.

The files in upstream/ refer to each other by ``file:`` addresses and declare
different drafts. This module loads them into one registry, without changing a
file on disk, so that any part of them can be used as a validator.
"""

import json
from functools import cache
from pathlib import Path

import jsonschema
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT7

UPSTREAM = Path(__file__).parent.parent / "upstream" / "schema"
BASE = "https://upstream.invalid/"
RECORD_FORMAT = "CVE_Record_Format.json"
IMPORTS = (
    "imports/cvss/cvss-v2.0.json",
    "imports/cvss/cvss-v3.0.json",
    "imports/cvss/cvss-v3.1.json",
    "imports/cvss/cvss-v4.0.json",
    "tags/adp-tags.json",
    "tags/cna-tags.json",
    "tags/reference-tags.json",
)


def load(name):
    return json.loads((UPSTREAM / name).read_text(encoding="utf-8"))


def _resolved(node):
    """A copy of a schema with each ``file:`` reference made absolute."""
    if isinstance(node, dict):
        return {
            key: BASE + value.removeprefix("file:")
            if key == "$ref" and isinstance(value, str) and value.startswith("file:")
            else _resolved(value)
            for key, value in node.items()
        }
    if isinstance(node, list):
        return [_resolved(item) for item in node]
    return node


@cache
def _registry():
    registry = Registry()
    for name in (RECORD_FORMAT, *IMPORTS):
        contents = _resolved(load(name))
        contents.pop("id", None)
        contents["$id"] = BASE + name
        contents["$schema"] = "http://json-schema.org/draft-07/schema#"
        registry = registry.with_resource(
            BASE + name, Resource.from_contents(contents, default_specification=DRAFT7)
        )
    return registry


def validator(path):
    """A validator for a path such as ``CVE_Record_Format.json#/definitions/product``."""
    # "file#/" names the whole file, which a JSON pointer writes as "file#".
    target = BASE + path.removesuffix("/") if path.endswith("#/") else BASE + path
    schema = {"$schema": "http://json-schema.org/draft-07/schema#", "$ref": target}
    return jsonschema.Draft7Validator(schema, registry=_registry())


def is_valid(instance, path):
    return validator(path).is_valid(instance)


def resolve_pointer(path):
    """The node of an upstream file that a path names, or KeyError."""
    name, _, pointer = path.partition("#")
    node = load(name)
    for part in pointer.strip("/").split("/") if pointer.strip("/") else []:
        node = node[int(part)] if isinstance(node, list) else node[part]
    return node

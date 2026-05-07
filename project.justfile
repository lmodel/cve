## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# Validate upstream CVE schema JSON examples against the bundled JSON Schema
test-third-party:
    uv run python -m pytest tests/test_third_party.py -v

# Run Python unit tests and upstream JSON validation
test-all: test test-third-party

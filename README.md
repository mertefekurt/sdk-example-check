# sdk-example-check

> Audit SDK examples for hardcoded keys, missing errors, and outdated imports.

## Operator guide Overview

Audit SDK examples for hardcoded keys, missing errors, and outdated imports. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts SDK example file. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
sdk-example-check examples/sample.txt
sdk-example-check examples/sample.txt --json --fail-on medium
python -m sdk_example_check --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `hardcoded-key` | high | API key appears hardcoded |
| `missing-errors` | medium | error handling is missing |
| `old-import` | low | outdated import noted |

## Validation Notes

```bash
ruff check .
pytest
python -m sdk_example_check --help
```

Example risky input:

```text
api_key sk_live_123 error handling missing old_import true
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.

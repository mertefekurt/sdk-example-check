<img src="assets/readme-cover.svg" alt="SDK Example Check cover" width="100%" />

# SDK Example Check

Audit SDK examples for hardcoded keys, missing errors, and outdated imports.

![stack](https://img.shields.io/badge/stack-Python-dc2626?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-7c3aed?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-0891b2?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-b45309?style=flat-square)

## Workflow

1. Collect the review notes or exported records.
2. Run `sdk-example-check` against the file.
3. Read the findings in Markdown, or switch to JSON for automation.
4. Fail CI only at the severity level you care about.

## Checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `hardcoded-key` | high | API key appears hardcoded |
| `missing-errors` | medium | error handling is missing |
| `old-import` | low | outdated import noted |

## Command line

```bash
python -m pip install -e ".[dev]"
sdk-example-check examples/sample.txt
sdk-example-check examples/sample.txt --json --fail-on medium
```

## Sample risky input

```text
api_key sk_live_123 error handling missing old_import true
```

## Project shape

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

# SDK Example Check

Audit SDK examples for hardcoded keys, missing errors, and outdated imports. I keep it small because this kind of check is most useful when it can run beside the work, not after the work has already shipped.

<img src="assets/readme-cover.svg" alt="SDK Example Check cover" width="100%" />

## Review checklist

- [ ] API key appears hardcoded (`hardcoded-key`, high)
- [ ] error handling is missing (`missing-errors`, medium)
- [ ] outdated import noted (`old-import`, low)

## Command path

```bash
git clone https://github.com/mertefekurt/sdk-example-check.git
cd sdk-example-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
sdk-example-check examples/sample.txt
sdk-example-check examples/sample.txt --json
```

## Fixture worth keeping

```text
api_key sk_live_123 error handling missing old_import true
```

## Files I look at first

```text
.github/        CI workflow
examples/       sample inputs
src/            package source
tests/          test coverage
.gitignore      project file
pyproject.toml  package metadata
```

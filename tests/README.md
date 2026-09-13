# Test qualification

Run the full retained suite from the repository root in a dedicated environment:

```bash
python -m pip install -e '.[dev]'
PYTHONPATH=src python -m pytest --import-mode=importlib -q tests
```

All 347 tests passed in the 2026-09-13 Python 3.13 qualification. The run reports
two imported-dataclass collection warnings and 29 Click isolated_filesystem
deprecation warnings.

Generated contract suites now import the current package. Async methods are
awaited, mocks use current signatures, network errors are injected at the
aiohttp boundary, and attribution uses valid ManifestEntry values through
ManifestManager.lookup. CLI scenarios use the current options/arguments and
collaborators, including controlled API startup and cleanup without a provider
request or long-running listener. Status tests check the package version,
counts, and integration configuration flags named by the supported API. The
source contract requires configuration flags but does not prescribe the
previous fixture's invented auto_fix_enabled/manual_review_required fields.

No tests are removed, skipped, or marked as expected failures as part of this
qualification. Mocked integration tests establish local behavior, not live
provider or deployment readiness.

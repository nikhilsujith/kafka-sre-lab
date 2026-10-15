# 0003. Python quality tooling

- Status: Accepted
- Date: 2026-10-15

## Context

The tools must be production-quality and reviewable, and CI must catch problems before review.

## Decision

`ruff` for linting, `black` for formatting, `mypy --strict` for types, `pytest` with
`pytest-cov` for tests, and `pre-commit` (including `gitleaks`) to run checks before every
commit. `make check` runs exactly what CI runs.

## Consequences

Strict typing adds some upfront effort on the dataclass models and pays back in refactors.
Coverage gate starts at 0 and rises to 80% at the end of Week 2.

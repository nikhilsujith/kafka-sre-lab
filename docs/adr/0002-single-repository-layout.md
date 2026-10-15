# 0002. One repository for application, infrastructure and operations

- Status: Accepted
- Date: 2026-10-15

## Context

The project spans Python code, Terraform, Kubernetes manifests, Helm charts, monitoring rules
and operational documents. These change together: a new metric touches the exporter, the alert
rule, the dashboard and the runbook.

## Decision

Keep everything in one repository with a top-level directory per concern (`src/`, `infra/`,
`deploy/`, `observability/`, `docs/`). Python uses the `src/` layout so tests run against the
installed package, not the working directory.

## Alternatives considered

| Option | Pros | Cons |
| --- | --- | --- |
| One repo (chosen) | Atomic changes across layers; one CI; easy to review | CI must path-filter as it grows |
| Separate app and infra repos | Matches some company setups; separate permissions | Cross-repo changes; harder to follow as a portfolio |

## Consequences

A reviewer can follow one feature from code to alert in a single pull request. CI jobs will be
path-filtered once Terraform and Helm jobs are added.

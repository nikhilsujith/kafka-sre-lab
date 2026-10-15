# 0001. Record architecture decisions

- Status: Accepted
- Date: 2026-10-15

## Context

This project makes many choices that have credible alternatives (concurrency model, Terraform
state layout, raw StatefulSet versus an operator). Without a record, the reasoning is lost and
reviewers only see the outcome.

## Decision

Every decision with a credible alternative gets a short ADR in `docs/adr/`, numbered in order,
using `0000-template.md`.

## Consequences

Decisions are reviewable in pull requests and can be explained in interviews. ADRs are never
edited after acceptance; a new ADR supersedes an old one.

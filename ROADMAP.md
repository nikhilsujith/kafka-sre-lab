# Roadmap

Each week extends the same system. Status values: Planned, In progress, Done.

| Week | Deliverable | Status |
| --- | --- | --- |
| 1 | `host-status`: dataclass health model fed by `/proc`, systemd and a JMX-named metrics snapshot; exit codes 0 to 3 | In progress |
| 2 | `health-checker`: concurrent TCP, TLS-expiry and HTTP checks with retries, JSON logs, packaging, 80% coverage | Planned |
| 3 | 3-tier VPC built by hand; SSM access; Flow Logs and tcpdump evidence | Planned |
| 4 | EC2 behind an HTTPS ALB with autoscaling, Route 53 and ACM | Planned |
| 5 | Terraform `network` module; idempotency and drift exercise | Planned |
| 6 | Remote state with locking; `compute` module; dev and prod environments | Planned |
| 7 | Container image (non-root, scanned) deployed to a local cluster with probes | Planned |
| 8 | Kafka as a StatefulSet; five injected failures diagnosed and written up | Planned |
| 9 | Default-deny NetworkPolicy, least-privilege RBAC, Helm chart | Planned |
| 10 | Prometheus metrics, Grafana dashboard, SLO doc, burn-rate alerts, runbooks | Planned |
| 11 | Chaos experiments, log aggregation, blameless postmortem | Planned |
| 12 | Messaging platform design doc, Postgres query tuning, STRIDE threat model | Planned |
| 13 to 14 | Timed algorithm practice (see `practice/log.md`) | Planned |
| 15 | CI/CD with security gates and Argo CD GitOps | Planned |
| 16 | Final README, demo recording, published docs | Planned |

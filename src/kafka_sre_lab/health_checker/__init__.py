"""health_checker: concurrent TCP, TLS and HTTP checks across many hosts (Week 2).

Planned layout: config.py (TOML targets), checks/ (tcp, tls, http), runner.py
(bounded concurrency, retries with backoff and jitter), logging_setup.py (JSON logs
with run_id), cli.py. Week 7 adds a `serve` mode; Week 10 adds /metrics.
"""

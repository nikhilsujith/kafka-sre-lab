"""Apply thresholds to models and produce HealthCheck results.

TODO (Week 1):
    - evaluate_broker(broker, thresholds, now) -> HealthCheck
    - evaluate_cluster(cluster, thresholds, now) -> (status, list[HealthCheck])
    - every breach adds a readable reason, e.g. "disk_pct 92.0 >= critical 90"
    - overall status is the worst status found; stale data (> 5 min) is UNKNOWN

Take `now` as a parameter instead of calling datetime.now() so tests are deterministic.
"""

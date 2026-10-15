"""Load a broker metrics snapshot from JSON into model objects.

TODO (Week 1):
    - parse ISO-8601 timestamps into timezone-aware datetimes
    - convert nested dicts into Host / BrokerMetrics / Broker / Cluster
    - on malformed input, raise an error naming the broker_id and field

See tests/fixtures/snapshots/healthy_and_critical.json for the input shape.
"""

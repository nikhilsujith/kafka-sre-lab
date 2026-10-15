"""Health data model. Pure data and validation; no file, network or process I/O.

TODO (Week 1):
    - HealthStatus enum, ordered by severity: HEALTHY < DEGRADED < CRITICAL < UNKNOWN
    - Host (frozen): hostname, ip (validate with the ipaddress module), rack
    - HostFacts: mem_available_bytes, load_avg_1m, disk_pct, inode_pct, zombie_count,
      kafka_unit_active
    - BrokerMetrics: fields named after the JMX beans listed in the README
    - Thresholds (frozen): warn/critical pairs; validate warn <= critical
    - Broker, HealthCheck (reasons via field(default_factory=list)), Cluster

Validate in __post_init__ and raise ValueError naming the bad field.
"""

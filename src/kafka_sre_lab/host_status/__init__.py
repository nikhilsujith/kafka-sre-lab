"""host_status: model Kafka broker and host health as typed objects (Week 1).

Module layout:
    models.py       Dataclasses and the HealthStatus enum. No I/O.
    linux_facts.py  Reads live host state from /proc, statvfs and systemd.
    snapshot.py     Loads broker metric snapshots (JSON) into models.
    evaluate.py     Applies Thresholds to models and produces HealthCheck results.
    cli.py          argparse entry point, output formatting and exit codes.

Keeping I/O (linux_facts, snapshot, cli) apart from logic (models, evaluate) is what
makes the logic testable without a real Linux host or Kafka cluster.
"""

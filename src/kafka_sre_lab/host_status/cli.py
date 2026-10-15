"""Command-line entry point for host-status.

Exit codes follow the Nagios plugin convention so the tool can drop into cron or
an existing monitoring system:

    0 = HEALTHY, 1 = DEGRADED, 2 = CRITICAL, 3 = UNKNOWN or bad input
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="host-status",
        description="Report Kafka broker and host health from a metrics snapshot.",
    )
    parser.add_argument("snapshot", help="path to a broker metrics snapshot (JSON)")
    parser.add_argument("--format", choices=["table", "json"], default="table")
    parser.add_argument("--thresholds", help="path to a thresholds file (JSON)")
    parser.add_argument("--only-unhealthy", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    build_parser().parse_args(argv)
    # TODO (Week 1): load snapshot, collect host facts, evaluate, render, map status to exit code.
    print("host-status: not implemented yet (see ROADMAP.md, Week 1)", file=sys.stderr)
    return EXIT_UNKNOWN


if __name__ == "__main__":
    sys.exit(main())

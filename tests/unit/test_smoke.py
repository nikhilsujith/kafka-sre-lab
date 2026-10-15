"""Smoke tests that keep CI meaningful before the real tests exist.

Replace these with real behavior tests as each module is implemented.
"""

import json
from pathlib import Path

import kafka_sre_lab
from kafka_sre_lab.host_status import cli

FIXTURES = Path(__file__).parent.parent / "fixtures"


def test_package_has_version() -> None:
    assert kafka_sre_lab.__version__


def test_cli_parser_accepts_documented_flags() -> None:
    args = cli.build_parser().parse_args(
        ["snap.json", "--format", "json", "--thresholds", "t.json", "--only-unhealthy"]
    )
    assert args.format == "json"
    assert args.only_unhealthy is True


def test_snapshot_fixture_is_valid_json() -> None:
    data = json.loads((FIXTURES / "snapshots" / "healthy_and_critical.json").read_text())
    assert {b["broker_id"] for b in data["brokers"]} == {1, 2}

"""Allow `python -m kafka_sre_lab.host_status`."""

import sys

from kafka_sre_lab.host_status.cli import main

sys.exit(main())

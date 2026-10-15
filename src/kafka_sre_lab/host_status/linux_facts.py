"""Collect live host facts from Linux.

TODO (Week 1):
    - read MemAvailable from <proc_root>/meminfo (not MemFree; see notes.md)
    - load average from <proc_root>/loadavg
    - disk and inode usage for the Kafka log dir via os.statvfs
    - zombie count by scanning <proc_root>/*/stat for state "Z"
    - kafka unit state via subprocess.run(["systemctl", "is-active", unit], timeout=...)

Take proc_root as a parameter (default "/proc") so tests can point it at
tests/fixtures/proc instead of the real filesystem.
"""

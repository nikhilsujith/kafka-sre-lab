# Test fixtures

- `proc/`: a fake `/proc` tree. `meminfo` deliberately has low `MemFree` but high
  `MemAvailable` (mostly page cache), which is a healthy host. Add `<pid>/stat` files with
  state `Z` to test zombie counting.
- `snapshots/`: broker metric snapshots. Broker 1 is healthy; broker 2 breaches URP,
  ISR shrink and latency thresholds.

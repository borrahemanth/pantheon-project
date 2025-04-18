#!/bin/bash
# Usage: bash run_test_scenario.sh my_results_50mbps_10ms

echo "Running Pantheon experiment for: $1"
src/experiments/test.py local \
  --schemes "cubic bbr copa" \
  --runtime 60 \
  --data-dir experiments/$1

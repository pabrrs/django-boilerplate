#!/bin/sh

./scripts/format.sh
./scripts/lint.sh
./scripts/health.sh
./scripts/test.sh

# check for missing migrations
./scripts/makem.sh --check
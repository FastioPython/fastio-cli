#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh
pytest --cov=fastio_cli --cov=tests --color yes --cov-config=.coveragerc --cov-report=xml
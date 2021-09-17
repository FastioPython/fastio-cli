#!/usr/bin/env bash

set -e
set -x

bash ./scripts/lint.sh

# shellcheck disable=SC2068
pytest --cov=fastio_cli --cov=tests --cov-report=term-missing:skip-covered --cov-report=xml tests ${@}
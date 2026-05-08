#!/usr/bin/env bash
set -euo pipefail

URL="${1:-http://localhost:8000/health}"

curl -o /dev/null -s -w "status=%{http_code} time_total=%{time_total}\n" "$URL"

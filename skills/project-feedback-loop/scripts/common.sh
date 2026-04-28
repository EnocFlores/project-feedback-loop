# skills/project-feedback-loop/scripts/common.sh
#!/usr/bin/env bash
set -euo pipefail

pfl_timestamp() {
  date -u +"%Y-%m-%dT%H:%M:%SZ"
}

pfl_append_jsonl() {
  local file="$1"
  local line="$2"
  mkdir -p "$(dirname "$file")"
  printf '%s\n' "$line" >> "$file"
}


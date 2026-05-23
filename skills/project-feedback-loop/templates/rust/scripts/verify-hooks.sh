#!/usr/bin/env sh
set -eu

repo_root=$(git rev-parse --show-toplevel)
git_dir=$(git rev-parse --git-dir)

if [ "${git_dir#/}" = "$git_dir" ]; then
  git_dir="$repo_root/$git_dir"
fi

configured_hooks_path=$(git config --get core.hooksPath || true)

if [ -n "$configured_hooks_path" ]; then
  case "$configured_hooks_path" in
    /*) active_hooks_path="$configured_hooks_path" ;;
    *) active_hooks_path="$repo_root/$configured_hooks_path" ;;
  esac
else
  active_hooks_path="$git_dir/hooks"
  configured_hooks_path=".git/hooks"
fi

hook_file="$active_hooks_path/pre-commit"

if [ ! -f "$hook_file" ]; then
  printf '%s\n' "Git hooks are not fully active. Missing: pre-commit. Active hooks path: $active_hooks_path. Configured core.hooksPath: $configured_hooks_path. Run ./scripts/install-hooks.sh to install durable hook files." >&2
  exit 1
fi

printf '%s\n' "Git hooks active at $active_hooks_path (core.hooksPath=$configured_hooks_path)"

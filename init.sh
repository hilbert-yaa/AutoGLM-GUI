#!/usr/bin/env bash

# Project root
PROJECT_ROOT="/home/hilbertc/Projects/AI-Phone/AutoGLM-GUI"

# 1. Load environment variables from .env (if present)
if [ -f "$PROJECT_ROOT/.env" ]; then
  # Export all variables defined in .env
  set -a
  # shellcheck source=/dev/null
  source "$PROJECT_ROOT/.env"
  set +a
fi

# 2. Source the virtual environment
if [ -f "$PROJECT_ROOT/.venv/bin/activate" ]; then
  # shellcheck source=/dev/null
  source "$PROJECT_ROOT/.venv/bin/activate"
else
  echo "Virtual environment not found at $PROJECT_ROOT/.venv" >&2
fi

# 3. Add platform-tools to PATH (only if not already present)
PLATFORM_TOOLS="/home/hilbertc/Projects/AI-Phone/platform-tools"
case ":$PATH:" in
  *":$PLATFORM_TOOLS:"*) ;;
  *) export PATH="$PLATFORM_TOOLS:$PATH" ;;
esac
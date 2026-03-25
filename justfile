set shell := ["bash", "-c"]

# List all available recipes
help:
    @just --list

# Install dependencies and setup environment (installs uv if missing)
install:
    @echo "Checking for uv..."
    @if ! command -v uv > /dev/null; then \
        echo "uv not found. Installing uv..."; \
        curl -LsSf https://astral.sh/uv/install.sh | sh; \
    else \
        echo "uv is already installed."; \
    fi

    uv sync
    uv run pre-commit install
    uv run pre-commit install --hook-type commit-msg

# Format code using ruff
format:
    uv run ruff format .

# Lint code using ruff
lint:
    uv run ruff check . --fix

# Type check code using mypy
type-check:
    uv run mypy src

# Run tests using pytest
test args='':
    uv run pytest {{args}}

# Check commit messages using gitlint
commit-check msg_file:
    uv run gitlint --msg-filename {{msg_file}} || (echo "Gitlint error. Please refer to docs/commit.md for the correct commit format." && exit 1)

# Run security checks using bandit
security-check:
    uv run bandit -r src/

# Run all checks (format, lint, type-check, test)
check: format lint type-check test

# Run pre-commit on all files
pre-commit:
    uv run pre-commit run --all-files

# Build the package
build:
    uv build

# Remove temporary files and caches
clean:
    rm -rf .venv
    rm -rf .ruff_cache
    rm -rf .mypy_cache
    rm -rf .pytest_cache .coverage
    rm -rf dist
    find . -type d -name "__pycache__" -exec rm -rf {} +
    find . -type f -name "*.pyc" -delete

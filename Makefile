.PHONY: help init install update check format lint type-check test security-check pre-commit build clean run

# Default target
help:
	@echo "Available commands:"
	@echo "  init           - Initialize environment (install uv)"
	@echo "  install        - Install dependencies using uv and setup pre-commit"
	@echo "  update         - Update dependencies using uv"
	@echo "  check          - Run all checks (format, lint, type-check, test, security-check)"
	@echo "  run            - Run the FastAPI server"
	@echo "  build          - Build the package"
	@echo "  format         - Format code using ruff"
	@echo "  lint           - Lint code using ruff"
	@echo "  type-check     - Type check code using mypy"
	@echo "  security-check - Run security checks using bandit"
	@echo "  test           - Run tests using pytest"
	@echo "  commit-check   - Run commit message check using gitlint"
	@echo "  pre-commit     - Run pre-commit on all files"
	@echo "  clean          - Remove temporary files and caches"

# Initialize environment (check and install uv, git)
init:
	@echo "Checking for git..."
	@if ! command -v git > /dev/null; then \
		echo "git not found. Installing git..."; \
		if [ "$$(expr substr $$(uname -s) 1 5)" = "Linux" ]; then \
			sudo apt-get update && sudo apt-get install -y git; \
		elif [ "$$(uname)" = "Darwin" ]; then \
			brew install git; \
		fi; \
	else \
		echo "git is already installed."; \
	fi
	@echo "Checking for uv..."
	@if ! command -v uv > /dev/null; then \
		echo "uv not found. Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	else \
		echo "uv is already installed."; \
	fi
	@echo "Checking if project setup is needed..."
	@if [ -d "src/{project}" ]; then \
		echo "Starting project-specific setup..."; \
		python3 scripts/setup.py \
			$(if $(PROJECT),--project $(PROJECT)) \
			$(if $(DESCRIPTION),--description "$(DESCRIPTION)") \
			$(if $(LICENSE),--license $(LICENSE)) \
			$(if $(PYTHON),--python $(PYTHON)); \
	else \
		echo "Project already set up (src/{project} not found)."; \
	fi
	@echo "Environment initialization complete."

# Install dependencies using uv and setup pre-commit
install:
	uv sync
	uv run pre-commit install
	uv run pre-commit install --hook-type commit-msg

# Update dependencies using uv
update:
	uv lock --upgrade
	uv sync

# Internal helper to check if the project is still a template
IS_TEMPLATE = $(shell [ -d "src/{project}" ] && echo 1 || echo 0)

# Macro to skip command if it's a template
define skip_if_template
	@if [ "$(IS_TEMPLATE)" = "1" ]; then \
		echo "Template state detected. Skipping $(1)..."; \
	else \
		$(2); \
	fi
endef

# Format code using ruff
format:
	$(call skip_if_template,format,uv run ruff format .)

# Lint code using ruff
lint:
	$(call skip_if_template,lint,uv run ruff check . --fix)

# Type check code using mypy
type-check:
	$(call skip_if_template,type-check,uv run mypy src tests)

# Run tests using pytest
test:
	$(call skip_if_template,test,uv run pytest)

# Run commit message check using gitlint
commit-check:
	$(call skip_if_template,commit-check,uv run gitlint)

# Run security checks using bandit
security-check:
	$(call skip_if_template,security-check,uv run bandit -r src/)

# Check for debug statements
debug-check:
	$(call skip_if_template,debug-check,uv run pre-commit run debug-statements --all-files)

# Run the FastAPI server
run:
	$(call skip_if_template,run,uv run {project})

# Run all checks (format, lint, type-check, test, security-check)
check: format lint type-check security-check test

# Build the package
build:
	uv build

# Run pre-commit on all files
pre-commit:
	uv run pre-commit run --all-files

# Remove temporary files and caches
clean:
	rm -rf .venv
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	rm -rf .pytest_cache .coverage
	rm -rf dist
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

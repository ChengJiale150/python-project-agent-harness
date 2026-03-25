## Project Structure

```
python_harness/
├── src/
│   └── python_harness/      # Main source package
│       ├── main.py          # Application entry point
│       ├── api/             # API layer (routes, endpoints)
│       ├── core/            # Core components (config)
│       ├── db/              # Database layer
│       ├── models/          # Database models
│       ├── schemas/         # Pydantic request/response schemas
│       └── services/        # Business logic services
├── tests/                   # Test suite
│   ├── architecture/        # Architectural guardrail tests (pytest-archon)
│   ├── e2e/                 # End-to-end integration tests
│   └── unit/                # Unit tests
├── justfile                 # Task automation commands
└── pyproject.toml           # Project configuration and dependencies
```

## Code Style

#### FastAPI Best Practices
- **Pydantic Validation**: Use Pydantic models for request/response schemas with automatic data validation
- **Dependency Injection**: Use FastAPI's dependency injection system for shared logic (DB connections, auth, etc.)
- **Async First**: Prefer `async/await`, avoid `run_in_executor` for non-blocking I/O operations
- **Clean Layering**: Router → Service → Repository, keep path operation functions lean
- **Error Handling**: Use `HTTPException` for consistent error responses, business exceptions should be raised in Service layer

### Type Hinting
-   **Strict Typing**: We use `mypy` in strict mode. All functions and methods must have type annotations.
-   **Modern Syntax**: Use Python 3.10+ syntax (e.g., `str | None` instead of `Optional[str]`, `list[str]` instead of `List[str]`).
-   **Pydantic**: Use Pydantic models for data validation and configuration schemas.

## Development

### Environment
- **Python Management**: We use `uv` to manage the Python environment and dependencies.
- **Run Python**: Use `uv run` to execute Python scripts (NEVER use `python3` or `python`).
- **Add Dependencies**: Use `uv add <package>` to add new dependencies (NEVER directly modify `pyproject.toml`).

### Common Commands
We use `just` as our command runner to provide a consistent development interface:
- `just check`: Run all quality gates (format, lint, type-check, test).

### Workflow
1. **Understand**: Read relevant code to collect associated context to fully understand user instructions, coding styles, and architectural paradigms.
2. **Test First (TDD)**: Write unit tests first to define the expected behavior of new features or modifications. Run `uv run pytest <test_file>` to confirm they fail as expected.
3. **Modify**: Implement the changes or new features following existing code paradigms.
4. **Verify**: Run `uv run pytest <test_file>` again to ensure the implementation passes the new tests and doesn't break existing ones.
5. **Check**: Run `just check` to ensure overall code quality (linting, typing, security) and catch any regressions.

### Commit
Before committing your changes, please ensure that your code passes all quality checks and adheres to the commit message format. For detailed instructions, please refer to [commit.md](docs/commit.md).

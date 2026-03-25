## Project Structure

The project follows a layered architecture where dependencies flow from higher-level layers to lower-level layers.

## Code Style

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
- `just test <test_file>`: Run tests using pytest.
- `just check`: Run all quality gates (format, lint, type-check, test).

### Workflow
1. **Understand**: Read relevant code to collect associated context to fully understand user instructions, coding styles, and architectural paradigms.
2. **Test First (TDD)**: Write unit tests first to define the expected behavior of new features or modifications. Run `just test <test_file>` to confirm they fail as expected.
3. **Modify**: Implement the changes or new features following existing code paradigms.
4. **Verify**: Run `just test <test_file>` again to ensure the implementation passes the new tests and doesn't break existing ones.
5. **Check**: Run `just check` to ensure overall code quality (linting, typing, security) and catch any regressions.

### Commit
Before committing your changes, please ensure that your code passes all quality checks and adheres to the commit message format. For detailed instructions, please refer to [commit.md](docs/commit.md).

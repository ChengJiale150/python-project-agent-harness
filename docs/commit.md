## Commit Guidelines

We follow strictly enforced commit message rules using `gitlint`.

### Workflow
Before committing, follow these steps to ensure quality:

1.  **Check Changes**: Review your changes to ensure only intended modifications are included:
    ```bash
    git status
    git diff
    ```
2.  **Verify Quality**: Run the following command to ensure code quality and architecture compliance:
    ```bash
    just pre-commit
    ```
    This command runs linting, type checks, and architecture tests. Only proceed with the commit if all checks pass.

### Format
-   **Language**: All commit messages must be in **English**.
-   **Structure**: Follow [Conventional Commits](https://www.conventionalcommits.org/).
    ```
    <type>(<scope>): <subject>

    <body>
    ```
-   **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

### Rules
1.  **Title Length**: Maximum 100 characters.
2.  **Body Line Length**: Maximum 120 characters.
3.  **Forbidden Words**: Title must not contain "wip".
4.  **Body Requirement**: A body message is required.

### Example
```
feat(auth): add jwt authentication

Implement JWT token generation and validation.
- Add pyjwt dependency
- Create auth utility functions
- Update user login endpoint
```

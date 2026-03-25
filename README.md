<div align="center">

# 🚀 python-project-agent-harness (FastAPI Edition)

**Harness Engineering: Taming the "Vibe Coding" Chaos with Enterprise-Grade Rigor for Modern APIs.** 🌐
<br>

[![GitHub stars](https://img.shields.io/github/stars/ChengJiale150/python-project-agent-harness?style=flat-square&color=DAA520)](https://github.com/ChengJiale150/python-project-agent-harness/stargazers)
[![GitHub watchers](https://img.shields.io/github/watchers/ChengJiale150/python-project-agent-harness?style=flat-square)](https://github.com/ChengJiale150/python-project-agent-harness/watchers)
[![GitHub forks](https://img.shields.io/github/forks/ChengJiale150/python-project-agent-harness?style=flat-square)](https://github.com/ChengJiale150/python-project-agent-harness/network)

[English](./README.md) | [中文版](./README_ZH.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2ca5e0.svg)](http://mypy-lang.org/)
[![Security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Gitleaks](https://img.shields.io/badge/gitleaks-protected-blueviolet.svg)](https://github.com/gitleaks/gitleaks)

</div>

## 🌊 The "Vibe Coding" Trap

We've all been there: You're using a powerful Coding Agent. It's magical. You're "Vibe Coding"—features are flying out, UI is popping up, and everything seems perfect. 🪄

But then, the **"Vibe"** shifts. 📉

- **The AI "Drift"**: Without constraints, your Agent starts using three different ways to handle errors in the same file.
- **Hidden Debt**: Silent type errors and security vulnerabilities creep in while you're busy admiring the speed.
- **The Maintenance Nightmare**: Six months later, you realize your AI-generated codebase is a tangled web of inconsistent logic that no human (or machine) can easily fix.

**Why does this happen?** Because Agents, like developers, perform best when working within a defined system. Without a "harness," speed is just a shortcut to technical debt. 🚧

## 🛡️ Enter the Harness: The Enterprise Blueprint

This isn't just another Python template. It's a **Harness** inspired by real-world **Enterprise Development Workflows**. 🏢

In high-performance engineering teams, we don't rely on "good vibes" to maintain quality. We rely on **uncompromising processes**. We use strict linting, mandatory typing, and automated security gates to minimize human error.

**Our Philosophy is simple: If these rigorous processes work for humans, they are even more effective for Agents.** 🤖

By wrapping your Agent in this enterprise-grade harness, we solve the "Vibe Coding" problem through:

- 🧱 **Systemic Constraints**: We replace "AI drift" with a single, clear rulebook (Ruff ALL + Strict Mypy).
- 🔒 **Automated Trust**: We don't just "hope" the code is secure; we verify it automatically with Bandit and Gitleaks.
- 🔄 **Deterministic Verification**: We provide the Agent with a "Source of Truth" (`just check`). If the code doesn't pass the gate, it's not finished.
- 🏗️ **Architectural Guardrails**: We use `pytest-archon` to enforce strict layering (API -> Services -> DB), ensuring the codebase remains modular and clean as it scales.

**Stop Vibe Coding. Start Engineering with Agents.** 💎

## ✨ Key Advantages: Why This Harness?

- **🚀 Elevate AI Code Quality**: By enforcing uncompromising linting and typing rules, we force Coding Agents to generate production-ready code. No more "lazy" AI implementation; only clean, robust, and PEP-compliant code.
- **📚 Code as Documentation (The Ultimate Context)**: Standardized Google-style docstrings and strict typing transform your codebase into the **best possible context** for LLMs. High-quality code documentation leads to a virtuous cycle of higher-quality AI code generation.
- **🤝 Native Multi-Agent Collaboration**: Designed based on enterprise team standards, this harness provides the perfect framework for multiple Agents to work together. Clear boundaries, standardized interfaces, and unified commit conventions prevent "Agent Drift" in complex projects.
- **🔄 100% AI Loop Support**: With our rigorous automated quality gates (Ruff, Mypy, Bandit, Pytest), you can achieve a true closed-loop AI development cycle. The constraints are so tight that you can trust AI-generated features with minimal to zero manual human review.
- **🛡️ Security & Integrity**: Integrated [Bandit](https://github.com/PyCQA/bandit) and [Gitleaks](https://github.com/gitleaks/gitleaks) act as a digital immune system, ensuring Agents never compromise your project's security or leak sensitive data.

## 🎁 Using This Template: Your New Project in Minutes

> [!IMPORTANT]
> **Prerequisites & Environment Requirements:**
> - **Windows**: You **must** use [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install) (Ubuntu recommended). This harness relies on Unix-style commands.
> - **macOS**: Ensure [Homebrew](https://brew.sh/) is installed to manage system packages.
> - **All Platforms**: `just` must be installed on your system to support the automation commands.
> - *Ubuntu/WSL*: `sudo apt install just` or `curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin`
> - *macOS*: `brew install just`

Transform this harness into your own project by following these simple steps. This project is designed as a **Template Repository** with placeholders ready for replacement.

### 1. 📂 Create Your Repository
Click the **"Use this template"** button on GitHub to create a new repository based on this harness:
```bash
git clone https://github.com/chengjiale/python-project-agent-harness.git my-awesome-project
cd my-awesome-project
```

### 2. 📝 Configure Your Attributes
This template uses placeholders in `{variable}` format. **GitHub does not natively support string replacement**, so we provide an automated initialization process using `just install` followed by the setup script.

You can initialize the project in two ways:

#### **Option A: Interactive (Recommended for Humans)**
First install dependencies, then run the setup script and follow the prompts:
```bash
just install
uv run scripts/setup.py
```

#### **Option B: Command-line Arguments (Recommended for Agents)**
Provide all attributes directly to skip the prompts:
```bash
just install
uv run scripts/setup.py --project=my_project --description="My cool project" --python=3.12 --license=MIT
```

- Check and install `uv` (if not already installed).
- Replace all placeholders (like `python_harness`, `{description}`, etc.).
- Rename the `src/python_harness/` directory to your actual project name.
- Update the `.python-version` file.

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `python_harness` | Your project/package name (lowercase, no spaces) | `my_awesome_project` |
| `{description}` | A brief description of your project | `A high-performance data processor` |
| `{license}` | The license type for your project | `MIT` |
| `{python_version}` | Your target Python version | `3.12` |

### 3. 🛠️ Development Workflow
Once initialized, use the following commands to maintain your enterprise-grade harness:

- **`just install`**: Setup your local environment and pre-commit hooks.
- **`just run`**: Start the FastAPI development server.
- **`just check`**: Run all quality gates (Lint, Type, Security, Test).
- **`just test`**: Execute the test suite with coverage reports.

# 🏗️ Architecture & Design Rationale

This project follows a "Strict-by-Design" architecture to minimize human error and AI hallucinations.

### 📁 Directory Layout
- **`src/python_harness/`**: Uses the `src` layout with standardized FastAPI layers:
    - `api/`: Route definitions and versioning.
    - `core/`: Global configuration via `pydantic-settings`.
    - `services/`: Business logic with Dependency Injection.
    - `models/`: Database models.
    - `schemas/`: Pydantic models for request/response validation.
    - `db/`: Database session management.
- **`tests/`**: Separated into `unit`, `e2e`, and `architecture` (using `pytest-archon`). This clear distinction helps the Agent understand the scope of testing.
- **`docs/`**: API documentation is handled natively by FastAPI (Swagger/Redoc). Non-API docs are stored here as Markdown.
- **`scripts/`**: A home for complex automation that goes beyond simple justfile commands.

### ⚙️ Core Configuration
- **`pyproject.toml`**: The "Brain" of the project. It uses `hatchling` for builds and `uv` for reproducible environment management. Includes FastAPI-specific linting rules (Async, Pydantic).
- **`.pre-commit-config.yaml`**: The "Gatekeeper". Ensures no code enters the history without being verified by our strict ruleset.

## 🚀 Getting Started: The Zero-to-Hero Flow

We've simplified the setup into a deterministic path. This is designed so an Agent can spin up a fully compliant environment with zero ambiguity.

1. **Install Dependencies**:
   ```bash
   just install
   ```
   *Rationale: This not only installs dependencies with lockfile precision but also sets up all Git Hooks (including commit-msg linting). It transforms a raw repo into a guarded fortress.*


2. **Sync Environment**:
   ```bash
   just sync
   ```
   *Rationale: This synchronizes the environment after initialization changes.*

3. **Verify Everything**:
   ```bash
   just check
   ```
   *Rationale: This runs format, lint, type-check, and tests to ensure code quality and catch regressions.*

---

<div align="center">
Built with ❤️ for the AI Engineering Community.
</div>

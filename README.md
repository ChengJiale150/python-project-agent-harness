# 🛠️ python-project-agent-harness

> **Taming the "Vibe Coding" Chaos with Enterprise-Grade Rigor.** 🚀

English | [中文版](README_ZH.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2ca5e0.svg)](http://mypy-lang.org/)

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
- 🔄 **Deterministic Verification**: We provide the Agent with a "Source of Truth" (`make check`). If the code doesn't pass the gate, it's not finished.

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
> - **All Platforms**: `make` must be installed on your system to support the automation commands.
>   - *Ubuntu/WSL*: `sudo apt install build-essential`
>   - *macOS*: `brew install make` (or use Xcode Command Line Tools)

Transform this harness into your own project by following these simple steps. This project is designed as a **Template Repository** with placeholders ready for replacement.

### 1. 📂 Create Your Repository
Click the **"Use this template"** button on GitHub to create a new repository based on this harness. Or clone it manually:
```bash
git clone https://github.com/chengjiale/python-project-agent-harness.git my-awesome-project
cd my-awesome-project
```

### 2. 📝 Configure Your Attributes
This template uses placeholders in `{variable}` format. **GitHub does not natively support string replacement**, so we provide an automated initialization process within our `make init` command.

You can initialize the project in two ways:

#### **Option A: Interactive (Recommended for Humans)**
Simply run the command and follow the prompts:
```bash
make init
```

#### **Option B: Command-line Arguments (Recommended for Agents)**
Provide all attributes directly to skip the prompts:
```bash
make init PROJECT=my_project DESCRIPTION="My cool project" PYTHON=3.12 LICENSE=MIT
```

*The `make init` command will automatically:*
- Install `uv` and `git` if they are not already installed.
- Trigger `scripts/setup.py` to replace all placeholders (like `{project}`, `{description}`, etc.).
- Rename the `src/{project}/` directory to your actual project name.
- Update the `.python-version` file.

| Placeholder | Description | Example |
|-------------|-------------|---------|
| `{project}` | Your project/package name (lowercase, no spaces) | `my_awesome_project` |
| `{description}` | A brief description of your project | `A high-performance data processor` |
| `{license}` | The license type for your project | `MIT` |
| `{python_version}` | Your target Python version | `3.12` |

### 3. 🚀 Install & Verify
Now, you're ready to start engineering:
```bash
make install
make check
```

# 🏗️ Architecture & Design Rationale

This project follows a "Strict-by-Design" architecture to minimize human error and AI hallucinations.

### 📁 Directory Layout
- **`src/{project}/`**: Uses the `src` layout to ensure that your package is only importable when correctly installed. This prevents accidental imports of local modules and guarantees that your tests run against the built package, exactly as it will be in production.
- **`tests/`**: Separated into `unit` and `e2e` (End-to-End). This clear distinction helps the Agent understand the scope of testing—whether it's checking a single function or a full system flow.
- **`docs/`**: Documentation is treated as code. Using MkDocs, we ensure that as your Agent adds features, it also updates the documentation, keeping the project's knowledge base alive.
- **`scripts/`**: A home for complex automation that goes beyond simple Makefile commands, providing a playground for Agent-driven DevOps.

### ⚙️ Core Configuration
- **`pyproject.toml`**: The "Brain" of the project. It uses `hatchling` for standard-compliant builds and `uv` for lightning-fast, reproducible environment management. By centralizing all tool configs (Ruff, Mypy, Pytest) here, we give the Agent a single, clear rulebook to follow.
- **`.pre-commit-config.yaml`**: The "Gatekeeper". By using local hooks that call our Makefile, we ensure that no code—no matter how fast it was "Vibe Coded"—ever enters the history without being verified.

## 🚀 Getting Started: The Zero-to-Hero Flow

We've simplified the setup into a deterministic path. This is designed so an Agent can spin up a fully compliant environment with zero ambiguity.

1. **Bootstrap the Tooling**:
   ```bash
   make init
   ```
   *Rationale: This ensures `uv` and `git` are present. It eliminates "it works on my machine" issues by standardizing the toolchain first.*

2. **Sync the Environment**:
   ```bash
   make install
   ```
   *Rationale: This not only installs dependencies with lockfile precision but also sets up all Git Hooks (including commit-msg linting). It transforms a raw repo into a guarded fortress.*

3. **Verify Everything**:
   ```bash
   make check
   ```
   *Rationale: The first thing an Agent should do is verify that the baseline is healthy. This command runs the full quality gauntlet.*

## 🛠️ Common Operations: Automation & Verification

In this harness, every command is a verification step. We don't just "run code"; we **validate** it.

| Command | Why it exists |
|---------|---------------|
| `make init` | Standardizes the local environment for both Humans and Agents. |
| `make install` | Guarantees a reproducible dev environment with enforced Git Hooks. |
| `make check` | **The Master Gate.** Runs linting, formatting, type-checking, security scans, and tests in one go. |
| `make format` | Delegates the "style vibe" to Ruff, ensuring 100% consistent code layout. |
| `make type-check` | Enforces `strict` Mypy rules to catch logic errors before they become bugs. |
| `make security-check` | Automatically audits code for common vulnerabilities using Bandit. |
| `make docs-serve` | Provides instant feedback on documentation quality. |
| `make build` | Ensures the project is always in a "shippable" state. |
| `make clean` | Resets the workspace to a pristine state, clearing AI-generated artifacts. |

## 📜 Engineering Standards: The "Rules of the Game"

To maintain the integrity of the harness, all contributions (human or AI) must adhere to these core principles. This ensures that the project remains scalable and free of "AI Drift."

### 🐍 Coding Excellence
- **Unified Style**: We follow [PEP 8](https://peps.python.org/pep-0008/) enforced by Ruff. No debates, just consistent code.
- **Strict Typing**: Type hints are mandatory. Every function must pass `strict` Mypy checks to prevent silent runtime failures.
- **Documentation**: We use [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) docstrings. Clear documentation is part of the code, not an afterthought.

### 🤝 Disciplined Collaboration
- **Atomic Commits**: Follow [Conventional Commits](https://www.conventionalcommits.org/). This allows us to automate changelogs and track the evolution of features clearly.
- **Branching Strategy**: Use descriptive feature branches (e.g., `feat/auth-system`).
- **The "Check" Rule**: Never push code that hasn't passed `make check` locally. The CI is our final safety net, but quality starts at the local machine.

## 🗺️ The Developer's Journey: How to Build

When adding new capabilities to your project, follow this structured workflow to ensure maximum stability:

1.  **Code**: Implement your logic within `src/{project}/`. The `src` layout ensures your code is isolated and correctly packaged.
2.  **Test**: Add unit tests in `tests/unit/` and integration tests in `tests/e2e/`. Testing is the only way to prove your Agent's "vibe" is actually working.
3.  **Document**: Update the documentation in the `docs/` directory. Use `make docs-serve` to verify how your new API looks to other developers.
4.  **Verify**: Run `make check` to ensure your changes haven't introduced regressions, type errors, or security flaws.

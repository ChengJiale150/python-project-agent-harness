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
| :--- | :--- | :--- |
| `{project}` | Your project/package name | `my_awesome_project` |
| `{description}` | Brief project description | `A high-performance agent harness` |
| `{license}` | Project license type | `MIT` |
| `{python_version}` | Full Python version | `3.12` |

### 3. 🛠️ Development Workflow
Once initialized, use the following commands to maintain your enterprise-grade harness:

- **`make install`**: Setup your local environment and pre-commit hooks.
- **`make run`**: Start the FastAPI development server.
- **`make check`**: Run all quality gates (Lint, Type, Security, Test).
- **`make test`**: Execute the test suite with coverage reports.
- **`make docs-serve`**: Preview your automated documentation.

---

<div align="center">
Built with ❤️ for the AI Engineering Community.
</div>

# 🛠️ python-project-agent-harness

> **用企业级的严谨驯服“氛围感编程”（Vibe Coding）的混乱。** 🚀

[English](README.md) | 中文版

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://img.shields.io/badge/mypy-checked-2ca5e0.svg)](http://mypy-lang.org/)

## 🌊 “氛围感编程”（Vibe Coding）的陷阱

我们都经历过：你正在使用功能强大的 Coding Agent。这种感觉很奇妙。你正在进行“氛围感编程”——功能飞速实现，UI 瞬间弹出，一切看起来都完美无缺。🪄

但随后，**“氛围”**变了。📉

- **AI 的“漂移”**：在没有约束的情况下，你的 Agent 开始在同一个文件中使用三种不同的方式来处理错误。
- **隐形债务**：当你忙于惊叹开发速度时，静默的类型错误和安全漏洞正悄然滋生。
- **维护噩梦**：六个月后，你意识到你的 AI 生成的代码库是一个逻辑极度不一致的乱麻，无论是人类还是机器都难以轻易修复。

**如果速度最终导致死胡同，那么速度就毫无意义。** 🚧

## 🛡️ 引入 Harness：为什么发起这个项目？

这不仅仅是另一个 Python 模板。它是一个 **Harness（线束/门禁）**，旨在包裹你的 Coding Agent 并强制执行资深工程团队的纪律。

该 Harness 受到现实世界 **企业级开发工作流** 的启发。🏢

在高性能工程团队中，我们不依赖“良好的感觉”来维持质量。我们依赖**不妥协的流程**。我们使用严格的 Lint 检查、强制性的类型注解和自动化的安全门禁来最大限度地减少人为错误。

**我们的哲学很简单：如果这些严苛的流程对人类有效，那么它们对 Agent 来说会更加有效。** 🤖

通过将你的 Agent 包裹在这个企业级门禁中，我们解决了“氛围感编程”带来的问题：

- 🧱 **系统性约束**：我们用统一的规则书（Ruff ALL + Strict Mypy）取代了 AI 的随机性（AI Drift）。
- 🔒 **自动化的信任**：我们不仅“希望”代码是安全的；我们通过 Bandit 和 Gitleaks 进行自动验证。
- 🔄 **确定性验证**：我们为 Agent 提供了唯一的“真理来源”（`make check`）。如果代码不能通过门禁，它就没有完成。

**停止氛围感编程。开始与 Agent 一起进行真正的工程化开发。** 💎

## ✨ 核心优势：为什么要用这个 Harness？

- **🚀 提升 AI 代码质量**：通过强制执行不妥协的 Linting 和 Typing 规则，我们强制 Coding Agent 生成生产级别的代码。不再有“懒惰”的 AI 实现；只有干净、健壮且符合 PEP 规范的代码。
- **📚 代码即文档（极致上下文）**：标准化的 Google 风格注释和严格的类型定义将你的代码库转化为 LLM 的**最佳上下文**。高质量的代码文档会形成正向循环，显著提高 AI 的代码生成质量。
- **🤝 原生支持多 Agent 协作**：基于企业团队标准设计，该 Harness 为多个 Agent 共同开发提供了完美框架。清晰的边界、标准化的接口和统一的提交规范防止了复杂项目中的“Agent 逻辑漂移”。
- **🔄 100% AI 闭环支持**：凭借极致严密的自动化质量门禁（Ruff, Mypy, Bandit, Pytest），你可以实现真正的闭环 AI 开发流程。其约束力之强，使得人类开发者甚至可以实现**零人工 Review**。
- **🛡️ 安全与完整性**：集成的 [Bandit](https://github.com/PyCQA/bandit) 和 [Gitleaks](https://github.com/gitleaks/gitleaks) 构成了项目的“数字免疫系统”，确保 Agent 绝不会引入安全漏洞或泄露敏感数据。

## 🎁 使用此模板：数分钟内开启新项目

> [!IMPORTANT]
> **前提条件与环境要求：**
> - **Windows**：你**必须**使用 [WSL2](https://learn.microsoft.com/en-us/windows/wsl/install)（推荐使用 Ubuntu）。该 Harness 依赖于 Unix 风格的命令。
> - **macOS**：确保已安装 [Homebrew](https://brew.sh/) 来管理系统包。
> - **全平台**：系统必须安装 `make` 以支持自动化命令。
>   - *Ubuntu/WSL*: `sudo apt install build-essential`
>   - *macOS*: `brew install make` (或使用 Xcode 命令行工具)

通过以下简单步骤将此 Harness 转化为你自己的项目。本项目被设计为带有待替换占位符的 **Template Repository**。

### 1. 📂 创建你的仓库
点击 GitHub 上的 **"Use this template"** 按钮基于此 Harness 创建新仓库。或者手动克隆：
```bash
git clone https://github.com/chengjiale/python-project-agent-harness.git my-awesome-project
cd my-awesome-project
```

### 2. 📝 配置你的属性
此模板使用 `{variable}` 格式的占位符。**GitHub 原生不支持字符串替换**，因此我们在 `make init` 命令中提供了一个自动化的初始化流程。

你可以通过两种方式初始化项目：

#### **方案 A：交互式（推荐人类使用）**
只需运行命令并根据提示操作：
```bash
make init
```

#### **方案 B：命令行参数（推荐 Agent 使用）**
直接提供所有属性以跳过提示：
```bash
make init PROJECT=my_project DESCRIPTION="我的超酷项目" PYTHON=3.12 LICENSE=MIT
```

*`make init` 命令会自动执行：*
- 检查并安装 `uv` 和 `git`（如果尚未安装）。
- 触发 `scripts/setup.py` 替换所有占位符（如 `{project}`, `{description}` 等）。
- 将 `src/{project}/` 目录重命名为你的实际项目名称。
- 更新 `.python-version` 文件。

| 占位符 | 描述 | 示例 |
|-------------|-------------|---------|
| `{project}` | 你的项目/包名（小写，无空格） | `my_awesome_project` |
| `{description}` | 项目的简短描述 | `一个高性能数据处理器` |
| `{license}` | 项目的协议类型 | `MIT` |
| `{python_version}` | 目标 Python 版本 | `3.12` |

### 3. 🚀 安装与验证
现在，你已经准备好开始工程化开发了：
```bash
make install
make check
```

# 🏗️ 架构与设计理由

本项目遵循“设计即严格”的架构，以最大限度地减少人为错误和 AI 幻觉。

### 📁 目录布局
- **`src/{project}/`**：采用 `src` 布局，确保只有在正确安装后包才是可导入的。这防止了本地模块的误导入，并保证你的测试运行在构建好的包上，与生产环境完全一致。
- **`tests/`**：分为 `unit`（单元测试）和 `e2e`（端到端测试）。这种清晰的区分有助于 Agent 理解测试范围——是检查单个函数还是完整的系统流程。
- **`docs/`**：文档即代码。通过 MkDocs，我们确保当你的 Agent 添加新功能时，它也会更新文档，保持项目知识库的生命力。
- **`scripts/`**：用于存放超出简单 Makefile 命令的复杂自动化脚本，为 Agent 驱动的 DevOps 提供试验场。

### ⚙️ 核心配置
- **`pyproject.toml`**：项目的“大脑”。它使用 `hatchling` 进行符合标准的构建，并使用 `uv` 进行极速、可复现的环境管理。通过在这里集中所有工具配置（Ruff, Mypy, Pytest），我们给了 Agent 一个单一、清晰的规则书。
- **`.pre-commit-config.yaml`**：项目的“守门员”。通过使用调用 Makefile 的本地 Hook，我们确保没有任何代码——无论它被“氛围感编程”得有多快——在未经验证的情况下进入 Git 历史。

## 🚀 快速开始：从零到英雄

我们将设置简化为一条确定性的路径。这是为了让 Agent 能够以零歧义的方式启动一个完全合规的环境。

1. **引导工具链**：
   ```bash
   make init
   ```
   *设计理由：这确保了 `uv` 和 `git` 的存在。它通过首先标准化工具链来消除“在我的机器上能运行”的问题。*

2. **同步环境**：
   ```bash
   make install
   ```
   *设计理由：这不仅以锁文件级别的精度安装依赖，还设置了所有的 Git Hook（包括提交信息检查）。它将一个原始仓库转化为一座设防的堡垒。*

3. **验证一切**：
   ```bash
   make check
   ```
   *设计理由：Agent 应该做的第一件事就是验证基准环境是健康的。该命令会运行全套质量检查。*

## 🛠️ 常用操作：自动化与验证

在这个 Harness 中，每个命令都是一个验证步骤。我们不仅是“运行代码”，我们是在**验证**它。

| 命令 | 存在理由 |
|---------|---------------|
| `make init` | 为人类和 Agent 标准化本地环境。 |
| `make install` | 保证一个带有强制 Git Hook 的可复现开发环境。 |
| `make check` | **主门禁**。一键运行 Lint、格式化、类型检查、安全扫描和测试。 |
| `make format` | 将“风格偏好”交给 Ruff，确保 100% 一致的代码布局。 |
| `make type-check` | 强制执行 `strict` Mypy 规则，在逻辑错误变成 Bug 之前捕获它们。 |
| `make security-check` | 使用 Bandit 自动审计代码中的常见漏洞。 |
| `make docs-serve` | 提供关于文档质量的即时反馈。 |
| `make build` | 确保项目始终处于“可交付”状态。 |
| `make clean` | 将工作区重置为原始状态，清理 AI 生成的工件。 |

## 📜 工程标准：“游戏规则”

为了保持 Harness 的完整性，所有贡献（无论是人类还是 AI）都必须遵守这些核心原则。这确保了项目保持可扩展性且不受“AI 逻辑漂移”的影响。

### 🐍 卓越编码
- **统一风格**：我们遵循由 Ruff 强制执行的 [PEP 8](https://peps.python.org/pep-0008/) 规范。无需争论，只有一致的代码。
- **严格类型**：类型提示是强制性的。每个函数都必须通过 `strict` Mypy 检查，以防止静默的运行时失败。
- **文档化**：我们使用 [Google 风格](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings) 的文档字符串。清晰的文档是代码的一部分，而不是事后的补救。

### 🤝 纪律严明的协作
- **原子化提交**：遵循 [约定式提交 (Conventional Commits)](https://www.conventionalcommits.org/)。这使我们能够自动化变更日志并清晰地追踪功能演进。
- **分支策略**：使用描述性的功能分支（例如 `feat/auth-system`）。
- **“Check”原则**：绝不推送未在本地通过 `make check` 的代码。CI 是我们最后的安全网，但质量始于本地机器。

## 🗺️ 开发者旅程：如何构建

在为你的项目添加新能力时，请遵循以下结构化工作流以确保最大的稳定性：

1.  **编码**：在 `src/{project}/` 中实现你的逻辑。`src` 布局确保了你的代码是隔离且正确打包的。
2.  **测试**：在 `tests/unit/` 中添加单元测试，在 `tests/e2e/` 中添加集成测试。测试是证明你的 Agent 生成的代码确实有效的唯一方法。
3.  **文档**：更新 `docs/` 目录中的文档。使用 `make docs-serve` 来验证你的新 API 对其他开发者来说是什么样的。
4.  **验证**：运行 `make check` 确保你的更改没有引入回归、类型错误或安全缺陷。

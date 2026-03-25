#!/usr/bin/env python3
import argparse
import re
import shutil
import sys
from pathlib import Path


SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]
PYC_SUFFIXES = {".pyc", ".pyo", ".pyd"}


def parse_gitignore(root_dir: Path) -> set[str]:
    """Parse .gitignore file and return set of patterns to ignore."""
    gitignore_path = root_dir / ".gitignore"
    if not gitignore_path.exists():
        return set()

    patterns = set()
    for line in gitignore_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        patterns.add(line)
    return patterns


def is_ignored_by_gitignore(path: Path, patterns: set[str], root_dir: Path) -> bool:
    """Check if a path matches any .gitignore pattern."""
    rel_path = path.relative_to(root_dir)
    path_str = str(rel_path)
    path_parts = rel_path.parts

    for pattern in patterns:
        if pattern.startswith("!"):
            continue
        if pattern.startswith("/"):
            if path_str == pattern[1:] or path_str.startswith(pattern[1:] + "/"):
                return True
        elif pattern.endswith("/"):
            dir_name = pattern.rstrip("/")
            if any(part == dir_name for part in path_parts):
                return True
        elif any(part == pattern or path_str == pattern for part in path_parts):
            return True
        elif "*" in pattern:
            regex = pattern.replace(".", r"\.").replace("**/", "(.+/)?")
            regex = re.sub(r"\*+", lambda m: ".*" if m.group().count("*") > 1 else "[^/]*", regex)
            if re.fullmatch(regex, path_str):
                return True

    return False


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments for project initialization."""
    parser = argparse.ArgumentParser(description="Initialize the Python Agent Harness project.")
    parser.add_argument("--project", help="Project/package name (lowercase, no spaces)")
    parser.add_argument("--description", help="Brief project description")
    parser.add_argument("--license", help="License type (default: MIT)")
    parser.add_argument(
        "--python",
        choices=SUPPORTED_PYTHON_VERSIONS,
        default="3.12",
        help="Target Python version (default: 3.12, must be >= 3.10)",
    )
    parser.add_argument(
        "--force", action="store_true", help="Force initialization even if src/python_harness is missing"
    )
    return parser.parse_args()


def get_project_config(args: argparse.Namespace) -> dict[str, str]:
    """Gather project configuration from arguments or interactive input."""
    project_name = args.project or input("Enter your project name (e.g., my_awesome_project): ").strip()
    description = args.description or input("Enter a brief description: ").strip()
    license_type = args.license or input("Enter license (default: MIT): ").strip() or "MIT"
    python_version = args.python

    if not project_name:
        print("❌ Error: Project name is required.")
        sys.exit(1)

    if not python_version or python_version not in SUPPORTED_PYTHON_VERSIONS:
        print(f"❌ Error: Python version must be one of {SUPPORTED_PYTHON_VERSIONS}.")
        sys.exit(1)

    return {
        "python_harness": project_name,
        "{description}": description,
        "{license}": license_type,
        "{python_version}": python_version,
        "{python_version_short}": python_version.replace(".", ""),
    }


def is_text_file(path: Path) -> bool:
    """Check if a file is a text file that can be read as UTF-8."""
    if path.suffix.lower() in PYC_SUFFIXES:
        return False
    if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".ico", ".pdf", ".zip", ".tar", ".gz", ".whl"}:
        return False
    try:
        path.read_text(encoding="utf-8")
        return True
    except (UnicodeDecodeError, ValueError):
        return False


def update_file_content(path: Path, replacements: dict[str, str]) -> bool:
    """Update placeholders and special cases in a single file. Returns True if updated."""
    try:
        content = path.read_text(encoding="utf-8")
        new_content = content

        template_name = "python_harness"
        project_name = replacements.get("python_harness", "")
        if template_name in new_content and project_name:
            new_content = new_content.replace(template_name, project_name)

        for key, value in replacements.items():
            new_content = new_content.replace(key, value)

        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  ✅ Updated: {path.name}")
            return True
        return False
    except (UnicodeDecodeError, ValueError):
        return False


def process_files(root_dir: Path, replacements: dict[str, str]) -> None:
    """Iterate through project files and replace placeholders."""
    exclude_dirs = {".git", ".venv", ".ruff_cache", ".mypy_cache", ".pytest_cache", "dist", "build", "__pycache__"}
    exclude_files = {"setup.py"}
    gitignore_patterns = parse_gitignore(root_dir)

    print("📝 Replacing placeholders in files...")
    for path in root_dir.rglob("*"):
        if any(part in exclude_dirs for part in path.parts):
            continue
        if not path.is_file():
            continue
        if path.name in exclude_files:
            continue
        if path.suffix.lower() in PYC_SUFFIXES:
            continue
        if is_ignored_by_gitignore(path, gitignore_patterns, root_dir):
            continue
        update_file_content(path, replacements)


def rename_source_dir(root_dir: Path, project_name: str) -> None:
    """Rename the template source directory to the actual project name."""
    src_placeholder = root_dir / "src" / "python_harness"
    new_src_dir = root_dir / "src" / project_name

    if src_placeholder.exists():
        print(f"📂 Renaming source directory to {project_name}...")
        if new_src_dir.exists() and new_src_dir != src_placeholder:
            shutil.rmtree(new_src_dir)
        src_placeholder.rename(new_src_dir)
        print(f"  ✅ Renamed: src/python_harness -> src/{project_name}")


def setup_project() -> None:
    """Main entry point for project setup."""
    args = parse_arguments()
    root_dir = Path(__file__).parent.parent

    # Check if project setup is actually needed
    src_placeholder = root_dir / "src" / "python_harness"
    if not src_placeholder.exists() and not args.force:
        print("ℹ️ Project already initialized or src/python_harness directory missing. Use --force to run anyway.")
        return

    print("🚀 Starting project initialization...")
    config = get_project_config(args)

    process_files(root_dir, config)
    rename_source_dir(root_dir, config["python_harness"])

    # Update .python-version separately
    pv_file = root_dir / ".python-version"
    if pv_file.exists():
        pv_file.write_text(config["{python_version}"] + "\n")
        print("✅ Updated .python-version")

    print("\n🎉 Project initialized successfully!")
    print(f"Next steps:\n  1. cd {root_dir}\n  2. just install\n  3. just check")


if __name__ == "__main__":
    setup_project()

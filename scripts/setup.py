#!/usr/bin/env python3
import argparse
import shutil
import sys
from pathlib import Path


SUPPORTED_PYTHON_VERSIONS = ["3.10", "3.11", "3.12", "3.13"]


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


def update_file_content(path: Path, replacements: dict[str, str]) -> None:
    """Update placeholders and special cases in a single file."""
    try:
        content = path.read_text(encoding="utf-8")
        new_content = content

        # Replace python_harness with actual project name
        template_name = "python_harness"
        project_name = replacements.get("python_harness", "")
        if template_name in new_content and project_name:
            new_content = new_content.replace(template_name, project_name)

        # Replace other placeholders
        for key, value in replacements.items():
            new_content = new_content.replace(key, value)

        if new_content != content:
            path.write_text(new_content, encoding="utf-8")
            print(f"  ✅ Updated: {path.name}")
    except Exception as e:
        print(f"  ⚠️ Skipped: {path.name} (Error: {e})")


def process_files(root_dir: Path, replacements: dict[str, str]) -> None:
    """Iterate through project files and replace placeholders."""
    exclude_dirs = {".git", ".venv", ".ruff_cache", ".mypy_cache", ".pytest_cache", "dist", "build"}
    exclude_files = {"setup.py", ".python-version"}

    print("📝 Replacing placeholders in files...")
    for path in root_dir.rglob("*"):
        if any(part in exclude_dirs for part in path.parts):
            continue
        if path.is_file() and path.name not in exclude_files:
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

#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path

def setup_project():
    """Setup the project by replacing placeholders in files and renaming directories."""
    parser = argparse.ArgumentParser(description="Initialize the Python Agent Harness project.")
    parser.add_argument("--project", help="Project/package name (lowercase, no spaces)")
    parser.add_argument("--description", help="Brief project description")
    parser.add_argument("--license", help="License type (default: MIT)")
    parser.add_argument("--python", help="Target Python version (default: 3.12)")
    parser.add_argument("--force", action="store_true", help="Force initialization even if src/{project} is missing")

    args = parser.parse_args()

    print("🚀 Starting project initialization...")

    # Interactive input if not provided via arguments
    project_name = args.project or input("Enter your project name (e.g., my_awesome_project): ").strip()
    description = args.description or input("Enter a brief description: ").strip()
    license_type = args.license or input("Enter license (default: MIT): ").strip() or "MIT"
    python_version = args.python or input("Enter Python version (default: 3.12): ").strip() or "3.12"

    if not project_name:
        print("❌ Error: Project name is required.")
        sys.exit(1)

    python_version_short = python_version.replace(".", "")
    
    replacements = {
        "{project}": project_name,
        "{description}": description,
        "{license}": license_type,
        "{python_version}": python_version,
        "{python_version_short}": python_version_short,
    }

    # Files and directories to exclude from replacement
    exclude_dirs = {".git", ".venv", ".ruff_cache", ".mypy_cache", ".pytest_cache", "dist", "build"}
    exclude_files = {"setup.py", ".python-version"}

    root_dir = Path(__file__).parent.parent
    
    # Check if project setup is actually needed
    src_placeholder = root_dir / "src" / "{project}"
    if not src_placeholder.exists() and not args.force:
        print("ℹ️ Project already initialized or src/{project} directory missing. Use --force to run anyway.")
        return

    # 1. Replace placeholders in files
    print("📝 Replacing placeholders in files...")
    for path in root_dir.rglob("*"):
        if any(part in exclude_dirs for part in path.parts):
            continue
        if path.is_file() and path.name not in exclude_files:
            try:
                content = path.read_text(encoding="utf-8")
                new_content = content
                for key, value in replacements.items():
                    new_content = new_content.replace(key, value)
                
                if new_content != content:
                    path.write_text(new_content, encoding="utf-8")
                    print(f"  ✅ Updated: {path.relative_to(root_dir)}")
            except Exception as e:
                print(f"  ⚠️ Skipped: {path.relative_to(root_dir)} (Error: {e})")

    # 2. Rename src/{project} directory
    new_src_dir = root_dir / "src" / project_name
    if src_placeholder.exists():
        print(f"📂 Renaming source directory to {project_name}...")
        if new_src_dir.exists() and new_src_dir != src_placeholder:
            shutil.rmtree(new_src_dir)
        src_placeholder.rename(new_src_dir)
        print(f"  ✅ Renamed: src/{{project}} -> src/{project_name}")

    # 3. Update .python-version separately
    pv_file = root_dir / ".python-version"
    if pv_file.exists():
        pv_file.write_text(python_version + "\n")
        print("✅ Updated .python-version")

    print("\n🎉 Project initialized successfully!")
    print(f"Next steps:\n  1. cd {root_dir}\n  2. make install\n  3. make check")

if __name__ == "__main__":
    setup_project()

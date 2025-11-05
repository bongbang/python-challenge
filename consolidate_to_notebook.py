#!/usr/bin/env python
"""
Script to consolidate all challenge .py and .md files into a Jupyter notebook.
Creates all_challenges_consolidated.ipynb with markdown and code cells.
"""

import glob
import re
import subprocess
import sys
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from pathlib import Path


def parse_challenge_number(filename):
    """
    Parse challenge number from filename.
    Handles formats like: 3.py, 4.py, 5_1.py, 10.py
    Returns tuple (main_number, sub_number) for sorting.
    """
    match = re.match(r'(\d+)(?:_(\d+))?\.py$', filename)
    if match:
        main_num = int(match.group(1))
        sub_num = int(match.group(2)) if match.group(2) else 0
        return (main_num, sub_num)
    return None


def find_challenge_files():
    """Find all challenge .py and .md files."""
    py_files = []
    md_files = []

    # Find all .py files
    for filepath in glob.glob('*.py'):
        # Skip helpers and consolidate script
        if filepath not in ['helpers.py', 'consolidate_to_notebook.py']:
            if parse_challenge_number(filepath):
                py_files.append(filepath)

    # Find all .md files
    for filepath in glob.glob('*.md'):
        # Skip CLAUDE.md
        if filepath != 'CLAUDE.md':
            if parse_challenge_number(filepath.replace('.md', '.py')):
                md_files.append(filepath)

    return py_files, md_files


def sort_files(files):
    """Sort files by challenge number."""
    def sort_key(filepath):
        parsed = parse_challenge_number(filepath)
        return parsed if parsed else (999, 0)

    return sorted(files, key=sort_key)


def create_notebook(py_files, md_files):
    """Create Jupyter notebook with challenge content."""
    nb = new_notebook()

    # Add title
    nb.cells.append(new_markdown_cell('# Python Challenge Solutions'))

    # Process each challenge
    for py_file in sort_files(py_files):
        challenge_num = parse_challenge_number(py_file)

        # Try to find corresponding .md file
        md_file = None
        main_num, sub_num = challenge_num
        md_pattern = f"{main_num}"
        if sub_num > 0:
            md_pattern += f"_{sub_num}"

        for md in md_files:
            if md.startswith(md_pattern + '.md'):
                md_file = md
                break

        # Add markdown cell if .md file exists
        if md_file:
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    md_content = f.read().strip()
                nb.cells.append(new_markdown_cell(md_content))
            except Exception as e:
                print(f"Warning: Could not read {md_file}: {e}")

        # Add code cell with .py content
        try:
            with open(py_file, 'r', encoding='utf-8') as f:
                py_content = f.read().strip()

            # Add the code as a code cell
            nb.cells.append(new_code_cell(py_content))

            print(f"Added Challenge {main_num}" + (f'_1' if sub_num > 0 else ''))

        except Exception as e:
            print(f"Error processing {py_file}: {e}")

    return nb


def execute_notebook(notebook_path):
    """Execute notebook using jupyter nbconvert."""
    print(f"\nExecuting notebook...")

    try:
        result = subprocess.run(
            ['jupyter', 'nbconvert', '--execute', '--to', 'notebook', '--inplace', notebook_path],
            capture_output=True,
            text=True,
            check=True
        )
        print("Successfully executed all cells")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing notebook: {e}")
        print(f"stdout: {e.stdout}")
        print(f"stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: jupyter command not found. Please ensure Jupyter is installed.")
        return False


def main():
    """Main function."""
    print("Finding challenge files...")
    py_files, md_files = find_challenge_files()

    print(f"Found {len(py_files)} Python files")
    print(f"Found {len(md_files)} Markdown files")

    print("\nCreating notebook...")
    nb = create_notebook(py_files, md_files)

    output_file = 'all_challenges_consolidated.ipynb'
    print(f"\nSaving notebook to {output_file}...")

    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)

    print(f"OK Successfully created {output_file}")
    print(f"  Total cells: {len(nb.cells)}")

    # Execute the notebook
    execute_notebook(output_file)

    print(f"\nDone! Open {output_file} in Jupyter to view results.")


if __name__ == '__main__':
    main()

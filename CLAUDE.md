# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a collection of solutions to the [Python
Challenge](http://www.pythonchallenge.com/) puzzles. Each numbered
challenge (3, 4, 5, etc.) has a corresponding Python file with the solution
implementation.  The solutions are meant to run in the local machine's
Conda base environment, which is normally activated before a Claude session
is started

## Repository Structure

- **helpers.py** - Utility module providing shared functionality
  - `read_text(*paths)` - Loads text from local files or URLs (tries local first, then HTTP)
  - `extract_string(original, start_snippet, end_snippet, inclusive=True)` 
  - Extracts substrings between markers
- **N.py** - Solution to Python Challenge N (e.g., 3.py, 4.py, 5.py,
  5_1.py). When a solution is broken down into smaller parts, a suffix
maybe added to the file name in the form of N_m.py.
- **N.md** - Reference URLs for each challenge
- **challenge_N.html** - Downloaded challenge pages from pythonchallenge.com
- **all_challenges.ipynb** - Jupyter notebook containing multiple challenge solutions

## Running Challenges

Execute any challenge solution directly:

```bash
python 3.py
python 4.py
python 5.py
python 5_1.py
```

Each challenge is self-contained and uses helpers.py for common operations.

## Key Dependencies

- **requests** - Required by helpers.py for HTTP requests. It is already
  installed in the local machine's Conda base environment.
- **pickle** - Used in challenge 5 for deserialization
- **re** - Regular expressions for pattern matching (challenge 3)

## Common Patterns

The solutions follow these patterns:
- Read challenge data using `helpers.read_text()` (supports both local files and URLs)
- Use regex pattern matching for text extraction
- Iterate through data structures to find answers
- Print the final result to advance to the next challenge

## Python Environment

- Python 3.13+
- Compatible with standard library modules plus requests

## Working with this Repository

When implementing or debugging solutions:
1. Check the associated .md file for the challenge URL reference
2. Review the challenge HTML files if downloaded locally
3. Use helpers.py functions for consistent file/URL handling
4. Test solutions with the commands above

## Style Guide 

1. Use single quotes for strings and docstrings unless impractical to do so.

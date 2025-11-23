# Contributing to StudentHub

Thank you for your interest in contributing to StudentHub! This guide will help you get started with your first open source contribution.

## Getting Started

### Prerequisites
- Python 3.7 or higher
- Git installed on your machine
- A GitHub account

### Step 1: Fork and Clone

1. Fork this repository by clicking the "Fork" button at the top right
2. Clone your fork to your local machine:
   ```bash
   git clone https://github.com/YOUR-USERNAME/demo.git
   cd demo
   ```

### Step 2: Create a Branch

Always create a new branch for your work:
```bash
git checkout -b fix-issue-number
```

Example: `git checkout -b fix-issue-1` or `git checkout -b add-feature-xyz`

### Step 3: Make Your Changes

- Read the code and understand what it does
- Make your changes following our coding standards
- Test your changes thoroughly
- Keep your changes focused on one issue at a time

### Step 4: Commit Your Changes

Write clear commit messages:
```bash
git add .
git commit -m "Fix: Add error handling for invalid dates (Issue #1)"
```

Good commit message examples:
- `Fix: Validate grade range in add_grade method`
- `Feat: Add export to CSV functionality`
- `Docs: Update README with installation steps`
- `Test: Add unit tests for calculate_gpa`

### Step 5: Push and Create Pull Request

```bash
git push origin your-branch-name
```

Then go to GitHub and create a Pull Request with:
- A clear title describing what you did
- Reference to the issue number (e.g., "Fixes #1")
- Description of your changes
- Any testing you performed

## Coding Standards

### Python Style Guide
- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions
- Keep functions small and focused on one task

### Example of Good Code:
```python
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): List of numeric values

    Returns:
        float: The average value
    """
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)
```

## Issue Labels

We use labels to categorize issues:
- **good-first-issue**: Perfect for beginners
- **bug**: Something isn't working
- **enhancement**: New feature or improvement
- **documentation**: Documentation improvements
- **help-wanted**: We need your help!

## Getting Help

- Check [ISSUES.md](ISSUES.md) for available issues
- Comment on an issue to get assigned
- Ask questions in the issue comments if you're stuck
- Don't hesitate to ask for help!

## Code Review Process

1. A maintainer will review your Pull Request
2. They may suggest changes or improvements
3. Make the requested changes and push again
4. Once approved, your code will be merged!

## Tips for Success

- Start with "good-first-issue" labeled issues
- Read existing code to understand the project structure
- Test your changes before submitting
- One issue = one pull request (don't mix multiple fixes)
- Be patient and respectful in all interactions
- Celebrate your contribution! 🎉

## Questions?

If you have questions, feel free to:
- Open a new issue with the "question" label
- Comment on existing issues
- Reach out to the maintainers

Happy Contributing!

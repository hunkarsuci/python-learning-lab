# Contributing

Thank you for helping improve this Python course.

## Good contributions

- Fix an incorrect or unclear explanation.
- Add a focused example or learner exercise.
- Improve accessibility, spelling, or notebook organization.
- Report an example that behaves differently on a supported Python version.

Keep each pull request focused on one lesson or one type of improvement.

## Local workflow

1. Create a branch from the default branch.
2. Install the dependencies from `requirements.txt`.
3. Edit and run the affected notebook from top to bottom.
4. Restart the kernel and run it again to catch hidden state.
5. Clear all cell outputs before committing.
6. Run `python tools/validate_notebooks.py`.
7. Describe what changed and how you verified it in the pull request.

Do not commit virtual environments, Jupyter checkpoints, secrets, or
machine-specific kernel metadata.

## Style

- Use Python 3 syntax and descriptive names.
- Prefer small examples that teach one idea.
- Put explanations in Markdown cells and executable code in code cells.
- Explain intentional exceptions immediately before the example.
- Avoid dependencies unless they are essential to the lesson.

By participating, you agree to follow [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

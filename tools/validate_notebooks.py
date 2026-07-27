"""Validate course notebooks without requiring third-party packages."""

from __future__ import annotations

import ast
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def validate(path: Path) -> list[str]:
    """Return human-readable validation failures for one notebook."""
    failures: list[str] = []
    try:
        notebook = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        return [f"cannot read notebook: {error}"]

    cells = notebook.get("cells")
    if not isinstance(cells, list) or not cells:
        return ["notebook has no cells"]

    if cells[0].get("cell_type") != "markdown":
        failures.append("first cell must be a Markdown lesson introduction")

    kernel = notebook.get("metadata", {}).get("kernelspec", {})
    if kernel.get("name") != "python3":
        failures.append("kernel name must be portable 'python3'")

    for index, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            failures.append(f"cell {index} contains saved output")
        source = "".join(cell.get("source", []))
        try:
            ast.parse(source, filename=f"{path.name}:cell-{index}")
        except SyntaxError as error:
            failures.append(
                f"cell {index} has invalid syntax at line {error.lineno}: "
                f"{error.msg}"
            )
    return failures


def main() -> int:
    notebooks = sorted(ROOT.glob("*.ipynb"))
    if not notebooks:
        print("No notebooks found.")
        return 1

    failed = False
    for notebook in notebooks:
        failures = validate(notebook)
        if failures:
            failed = True
            print(f"FAIL {notebook.name}")
            for failure in failures:
                print(f"  - {failure}")
        else:
            print(f"PASS {notebook.name}")
    return int(failed)


if __name__ == "__main__":
    raise SystemExit(main())

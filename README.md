<div align="center">

# Python Learning Lab

**Learn Python by reading, running, and changing real examples.**

[![CI](https://github.com/hunkarsuci/python-learning-lab/actions/workflows/notebooks.yml/badge.svg?branch=main)](https://github.com/hunkarsuci/python-learning-lab/actions/workflows/notebooks.yml?query=branch%3Amain)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)](https://jupyter.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/hunkarsuci/python-learning-lab?style=flat&logo=github)](https://github.com/hunkarsuci/python-learning-lab/stargazers)

</div>

A growing, hands-on Python learning path built from scratch with Jupyter
notebooks, practical examples, exercises, and projects from fundamentals to
advanced Python development.

The lessons favor short, runnable examples that you can change and explore.
They are intended for learners who know how to open a Jupyter notebook but do
not need prior Python experience.

## Curriculum

| Order | Lesson | Topics | Status |
| ---: | --- | --- | :---: |
| 1 | [Python Basics](Python_Basics.ipynb) | Values, operators, strings, collections | Available |
| 2 | [Python Basics II](Python_Basics_II.ipynb) | Control flow, loops, functions, scope | Available |
| 3 | [Object-Oriented Programming](Advanced_Python_OOP.ipynb) | Classes, inheritance, polymorphism, MRO | Available |
| 4 | [Functional Programming](Advanced_Python_FunctionalProgramming.ipynb) | Pure functions, map/filter/reduce, comprehensions | Available |
| 5 | [Decorators](Advanced_Python_Decorators.ipynb) | Higher-order functions and decorators | Available |
| 6 | [Error Handling](Advanced_Python_Error_Handling.ipynb) | Exceptions, `try`/`except`, `else`, `finally` | Available |
| 7 | [Generators](Advanced_Python_Generators.ipynb) | Iterators, `yield`, generator functions, performance | Available |
| 8 | [Modules and Packages](Modules%20in%20Python/main.py) | Imports, modules, packages, and reusable functions | Available |
| 9 | [File Input and Output](File_Input_and_Output/FileOpenClose.py) | Reading/writing files, `open`/`close`, `with`, error handling | Available |

More lessons, exercises, and projects will be added as the learning path grows.

## Getting started

You need Python 3.10 or newer.

```bash
git clone https://github.com/hunkarsuci/python-learning-lab.git
cd python-learning-lab
python -m venv .venv
```

Activate the environment:

```text
Windows (PowerShell): .venv\Scripts\Activate.ps1
macOS/Linux:          source .venv/bin/activate
```

Then install and launch Jupyter:

```bash
python -m pip install -r requirements.txt
jupyter lab
```

Open the notebooks in curriculum order. Run cells one at a time and experiment
with the examples. A few lessons intentionally request keyboard input.

## Repository structure

```text
python-learning-lab/
├── Advanced_Python_Generators.ipynb
├── Python_Basics.ipynb
├── Python_Basics_II.ipynb
├── Advanced_Python_OOP.ipynb
├── Advanced_Python_FunctionalProgramming.ipynb
├── Advanced_Python_Decorators.ipynb
├── Advanced_Python_Error_Handling.ipynb
├── Modules in Python/
│   ├── main.py
│   ├── utility.py
│   └── shopping/
│       └── shopping_more/
│           └── shopping_cart.py
├── File_Input_and_Output/
│   ├── FileOpenClose.py
│   ├── FileReadWriteAppend.py
│   └── ExerciseTranslator.py
├── tools/
│   └── validate_notebooks.py
├── requirements.txt
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
└── LICENSE
```

Each lesson is a standalone notebook, making it easy to study the course in
order or revisit an individual topic.

## Repository checks

The repository includes a dependency-free notebook validator:

```bash
python tools/validate_notebooks.py
```

It checks notebook structure, portable Python kernel metadata, accidental saved
outputs, and Python syntax. GitHub Actions runs the same check for every push
and pull request.

## Contributing

Corrections, clearer explanations, exercises, and new examples are welcome.
Read [CONTRIBUTING.md](CONTRIBUTING.md), then open an issue or pull request with
a focused improvement. All participation follows our
[Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is available under the [MIT License](LICENSE).

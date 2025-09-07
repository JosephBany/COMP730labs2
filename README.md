# 21 Nim — OOP, Tests, Exceptions, and Docs

This project implements the classic **21 Nim** game using **object-oriented design**, with **unit tests**, **exception handling**, and consistent **Google-style docstrings**.

- **Variant**: Two players take turns removing 1–3 sticks from a pile starting at 21. **The player who takes the last stick wins.**
- **Design**: `NimGame` encapsulates game state and rules; `Player` represents participants; `InvalidMoveError` signals illegal moves; `cli.py` provides a simple console UI.
- **Docs**: Module, class, and method docstrings follow **Google style**. Replace the author in module docstrings with your real name.
- **Standards**: Package/module names adhere to **PEP 8** (lowercase, underscores).

## Project layout

```text
nim21_project/
├─ nim21/
│  ├─ __init__.py
│  ├─ exceptions.py
│  ├─ game.py
│  ├─ player.py
│  └─ cli.py
└─ tests/
   └─ test_game.py
```

## Requirements

- Python 3.9+ (standard library only; no third-party dependencies)

## Install (editable) and run

```bash
cd nim21_project
# (Optional) create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Run tests
python -m unittest discover -s tests -v

# Play from the package module
python -m nim21.cli
```

## Docstring style

We use **Google style** docstrings consistently across modules, classes, and methods.  
- **Module docstrings** include your name, date created (`2025-09-05`), and collaborators.  
- **Class docstrings** describe **class attributes**.  
- **Method docstrings** describe **parameters**, **return values**, and **raised exceptions**.  
- **Constructor docstrings** note instance attributes (documented either in class docstring or `__init__` docstring per style).  

## Exception handling

Invalid moves raise `InvalidMoveError` with clear messages. Input parsing in the CLI handles `ValueError` for non-integer input and continues prompting.

## Linting & style

- Names follow **PEP 8** (packages/modules: lowercase with underscores; classes: CapWords; functions/methods: lowercase with underscores).
- No orphan/floating top-level code—only `if __name__ == "__main__":` entry points.

## Attribution

- Collaborator: ChatGPT (AI assistant).

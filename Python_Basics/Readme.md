# Python Basics

Core Python, written with data engineering, data analytics and GenAI (LLM) integration in mind.
Every file can be run on its own, and the expected output is written as a comment next to each line.

Needs **Python 3.10+** (`match-case` in `conditionals.py` and the `float | None` type hint).

## Learning order

| # | File | What it covers |
|---|------|----------------|
| 1 | [Print.py](Print.py) | `print`, `sep` / `end`, f-strings, number formatting, table alignment, pretty JSON, `logging` |
| 2 | [variables.py](variables.py) | naming rules, dynamic typing, type hints, swapping, references, reading secrets from env variables |
| 3 | [DataTypes.py](DataTypes.py) | `int`, `float`, `bool`, `None`, float precision, `Decimal`, `NaN`, typecasting |
| 4 | [operators.py](operators.py) | arithmetic, comparison, logical, identity, membership, bitwise (and why pandas uses `&` `\|` `~`) |
| 5 | [strings.py](strings.py) | indexing, slicing, methods, cleaning text, split / join, prompt templates, encoding |
| 6 | [list.py](list.py) | list methods, sorting records, copying, comprehensions, de-duplication, 2D lists |
| 7 | [conditionals.py](conditionals.py) | `if` / `elif` / `else`, truthy & falsy, data quality checks, `match-case` |
| 8 | [loops.py](loops.py) | `for`, `while`, `range`, `enumerate`, `zip`, group-by with a dict, retries, batching |

## Run a file

```bash
cd Python_Basics
python3 strings.py
```

## Note on file names

Don't name a file after a Python module (`string.py`, `operator.py`, `json.py`, `random.py`, ...).
Python finds your file first, so `import logging` (which imports `string` internally) would load
your file instead of the real one. That's why these are named `strings.py` and `operators.py`.

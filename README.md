# python_cli_template

[![PyPI version](https://badgen.net/pypi/v/python_cli_template)](https://pypi.org/project/python_cli_template/)
[![codecov](https://codecov.io/gh/remarkablemark/python_cli_template/graph/badge.svg?token=l6pg0nf9aJ)](https://codecov.io/gh/remarkablemark/python_cli_template)
[![lint](https://github.com/remarkablemark/python_cli_template/actions/workflows/lint.yml/badge.svg)](https://github.com/remarkablemark/python_cli_template/actions/workflows/lint.yml)

🐍 Python CLI Template

## Quick Start

Greet a name:

```sh
pipx run python_cli_template --name world
```

## Prerequisites

- [Python](https://www.python.org/)
- [pipx](https://pipx.pypa.io/)

## CLI

Install the CLI:

```sh
pipx install python_cli_template
```

### `--name`

**Optional**: Name to greet. Defaults to `World`.

```sh
python_cli_template --name Alex
```

### `--version`

Show the program's version number and exit:

```sh
python_cli_template --version # python_cli_template -v
```

Show the help message and exit:

```sh
python_cli_template --help # python_cli_template -h
```

## Script

Create a virtual environment:

```sh
python3 -m venv .venv
```

Activate the virtual environment:

```sh
source .venv/bin/activate
```

Install the package:

```sh
pip install python_cli_template
```

Greet a name:

```py
# script.py
from python_cli_template import hello

print(hello("Bob"))
```

Run the script:

```sh
python script.py
```

## License

[MIT](https://github.com/remarkablemark/python_cli_template/blob/master/LICENSE)

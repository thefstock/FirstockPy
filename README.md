# Firstock Python Library and SDK

## License

This library is distributed under MIT License.

## Dependency management

The project uses [Poetry](https://python-poetry.org/) tool for managing dependencies and packaging. 

It is a good idea to familiarise yourself with basics of [Poetry](https://python-poetry.org/) and [basic usage](https://python-poetry.org/docs/basic-usage/) before you begin.

## Getting Started

### Installation

To get started you need to [install poetry](https://python-poetry.org/docs/#installation).
Run this command inside the ```py_client``` directory.
```bash
poetry install
```

### Code structure

This repo provides a Python SDK comprising of the primary client code written in Python and in addition to that you will find the associated documentations, helpful examples to get started and a test suite for unit testing.

- The primary client code project (library) can be found inside the ```client/py_client``` directory.
- The documentation for the client code can be found in ```client/docs``` directory in both HTML and Markdown formats. They are identical.
- Additionally, examples of how to use library can be found in ```client/examples``` directory.
- The tests can be found in the ```client/tests``` directory.

### Running the examples

Several examples can be found in ```client/examples``` directory which can be run as:
```bash
poetry run python -m examples.<module>.<method> [...args]
# you can run this command with --help flag to get arguments
```

For example, to Log in a User:

```bash
poetry run python -m examples.users.login --uid=TVEXAMPLE --factor2='1010101' --vc=APISOMEUSER --appkey=ncoAPIkeySomeKey1010101 --pwd=SomePwd
```

### Running the tests

```bash
poetry run pytest
```
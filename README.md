# todo

Make todo list via command line

[![Build](https://github.com/saeedou/todo/actions/workflows/build.yml/badge.svg)](https://github.com/saeedou/todo/actions/workflows/build.yml)
[![Coverage Status](https://coveralls.io/repos/github/saeedou/todo/badge.svg?branch=master)](https://coveralls.io/github/saeedou/todo?branch=master)

```bash
pip install .
todo completion install
```

## Running Tests

```bash
make env
make test
```

## How to use 

```
usage: todo [-h] [-v] [-c FILENAME] {list,l,completion} ...

Simple todo list

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show version
  -c FILENAME, --configfile FILENAME
                        Configuration file to load.

Sub commands:
  {list,l,completion}
    list (l)            Print the todo list.
    completion          Bash auto completion using argcomplete python package.

```

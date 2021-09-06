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
usage: todo [-h] [-v] [-c FILENAME] {list,l,append,add,a,delete,d,remove,r,search,s,completion} ...

Simple todo list

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         Show version
  -c FILENAME, --configfile FILENAME
                        Configuration file to load.

Sub commands:
  {list,l,append,add,a,delete,d,remove,r,search,s,completion}
    list (l)            Print the todo list.
    append (add, a)     Append item and description to the todo list.
    delete (d, remove, r)
                        To delete an item and its desctiption.
    search (s)          To print searched items(no argument print the whole list).
    completion          Bash auto completion using argcomplete python package.
```

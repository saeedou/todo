import os
import functools
import tempfile
import shutil

import pytest
from bddcli import Given, stdout,  Application, status, stderr, when, given

from todo import __version__ as todo_version


@pytest.fixture
def tempstruct():
    temp_directories = []

    def create_nodes(root, **kw):
        for k, v in kw.items():
            name = os.path.join(root, k)

            if isinstance(v, dict):
                os.mkdir(name)
                create_nodes(name, **v)
                continue

            if hasattr(v, 'read'):
                f = v
                v = f.read()
                f.close()

            with open(name, 'w') as f:
                f.write(v)

    def _make_temp_directory(**kw):
        """Structure example: {'a.html': 'Hello', 'b': {}}."""
        root = tempfile.mkdtemp()
        temp_directories.append(root)
        create_nodes(root, **kw)
        return root

    yield _make_temp_directory

    for d in temp_directories:
        shutil.rmtree(d)


cliapp = Application('todo', 'todo:Todo.quickstart')
GivenApp = functools.partial(Given, cliapp)


def read_db(path, mode='r'):
    with open(path, mode) as f:
        data = f.read()
    return data


@pytest.fixture
def app():
    return GivenApp


APPEND_ERROR = '''usage: todo append [-h] item [description]
todo append: error: the following arguments are required: item
'''
DELETE_ERROR = '''usage: todo delete [-h] item
todo delete: error: the following arguments are required: item
'''

N = '\n'


def test_version(app):
    with app():
        assert status == 0

        when('-v')
        assert stdout == todo_version + N
        assert stderr == ''
        assert status == 0

        when('--version')
        assert stdout == todo_version + N
        assert stderr == ''
        assert status == 0


def test_list(app, tempstruct):
    dbroot = tempstruct(bar='a\nb\n')
    temproot = tempstruct(
        foo=f'database:\n  filename: {dbroot}/bar'
    )

    with app(f'--configfile {temproot}/foo list'):
        assert stderr == ''
        assert stdout == 'a\nb\n'


def test_append(app, tempstruct):
    dbroot = tempstruct(bar='')
    temproot = tempstruct(
        foo=f'database:\n  filename: {dbroot}/bar'
    )

    with app(f'--configfile {temproot}/foo append'):
        assert stdout == ''
        assert stderr == APPEND_ERROR
        assert status == 2

        when(given + ' bar ')
        assert stdout == ''
        assert stderr == ''
        assert status == 0
        assert read_db(f'{dbroot}/bar') == 'bar:\t\n'

        when(given + ' qux ' + ' corge')
        assert stdout == ''
        assert stderr == ''
        assert status == 0
        assert read_db(f'{dbroot}/bar') == 'bar:\nqux:\tcorge\n'


def test_delete(app, tempstruct):
    dbroot = tempstruct(bar='baz:\tqux\ncorage:\tgrault')
    temproot = tempstruct(
        foo=f'database:\n  filename: {dbroot}/bar'
    )

    with app(f'--configfile {temproot}/foo delete'):
        assert stdout == ''
        assert stderr == DELETE_ERROR
        assert status == 2

        when(given + 'baz')
        assert stdout == ''
        assert stderr == ''
        assert status == 0
        assert read_db(f'{dbroot}/bar') == 'corage:\tgrault\n'

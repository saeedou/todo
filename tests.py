from bddcli import Given, stdout,  Application, status, stderr, when

from todo import __version__ as todo_version


N = '\n'
app = Application('todo', 'todo:Todo.quickstart')


def test_version():
    with Given(app):
        assert status == 0

        when('-v')
        assert stdout == todo_version + N
        assert stderr == ''
        assert status == 0

        when('--version')
        assert stdout == todo_version + N
        assert stderr == ''
        assert status == 0

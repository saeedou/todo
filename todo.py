from os import environ

from pymlconf import DeferredRoot
from easycli import Root, Argument, SubCommand


__version__ = '0.1.0'
HOME = environ['HOME']
BUILTINSETTINGS = f'''
database:
  filename: {HOME}/.cache/todo.csv
'''
settings = DeferredRoot()


class DB:
    def __init__(self):
        with open(self.filename) as dbfile:
            self.items = [line.strip() for line in dbfile]

    @property
    def filename(self):
        return settings.database.filename


def initialize_settings(configfile=None):
    settings.initialize(BUILTINSETTINGS)
    if configfile is not None:
        settings.loadfile(configfile)


class List(SubCommand):
    __command__ = 'list'
    __aliases__ = ['l']
    __help__ = 'Print the todo list.'

    def __call__(self, args):
        db = DB()
        for i in db.items:
            print(i)


class Todo(Root):
    __help__ = 'Simple todo list'
    __completion__ = True
    __arguments__ = [
        Argument(
            '-v', '--version',
            action='store_true',
            help='Show version'
        ),
        Argument(
            '-c', '--configfile',
            metavar='FILENAME',
            help='Configuration file to load.'
        ),
        List,
    ]

    def _execute_subcommand(self, args):
        initialize_settings(args.configfile)
        return super()._execute_subcommand(args)

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)

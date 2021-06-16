import easycli


__version__ = '0.1.0'


class Todo(easycli.Root):
    __help__ = 'Simple todo list'
    __completion__ = True
    __arguments__ = [
        easycli.Argument(
            '-v', '--version',
            action='store_true',
            help='Show version'
        ),
    ]

    def __call__(self, args):
        if args.version:
            print(__version__)
            return

        return super().__call__(args)

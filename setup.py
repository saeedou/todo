import re
from os.path import join, dirname
from setuptools import setup


with open(join(dirname(__file__), 'todo.py')) as f:
    version = re.match('.*__version__ = \'(.*?)\'', f.read(), re.S).group(1)


DEPENDENCIES = [
    'easycli',
]


setup(
    name='todo',
    version=version,
    py_modules=['todo'],
    description='make todo list via command line',
    include_package_data=True,
    install_requires=DEPENDENCIES,
    license='MIT',
    entry_points={
        'console_scripts': [
            'todo = todo:Todo.quickstart',
        ]
    }
)

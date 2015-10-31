try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'BigBrain',
    'packages': ['bigbrain'],
    'description': 'make strange games with this',
    'author': 'c',
    'url': 'http://github.com/connorwalsh/BigBrain.git',
    'author_email': 'c@polygon.pizza',
    'version': '0.0.0'
}

setup(**config)

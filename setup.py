try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Python Skeleton Project',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['source'],
    'name': 'python-skeleton'
}

setup(**config)
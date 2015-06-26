from setuptools import setup

__author__ = 'mocsar'

setup(
    name='csocso',
    version='0.1',
    py_modules=['csocso'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        csocso=csocso:cli
    ''',
)
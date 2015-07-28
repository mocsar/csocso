from setuptools import setup

__author__ = 'mocsar'

setup(
    name='csocso',
    version='0.1',
    py_modules=['csocso'],
    data_files=[('/etc/bash_completion.d', ['csocso-complete.sh'])],
    install_requires=[
        'Click',
        'pymongo',
        'trueskill'
    ],
    entry_points='''
        [console_scripts]
        csocso=csocso:cli
    ''',
)
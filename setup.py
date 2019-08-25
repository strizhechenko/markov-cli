#!/usr/bin/env python

'''Heil to combinatoric explosion reduce!'''

import os

from setuptools import setup, find_packages


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


setup(
    name='markov-cli',
    version='0.0.1',
    author='Oleg Strizhechenko',
    author_email='oleg.strizhechenko@gmail.com',
    license='GPL',
    url='https://github.com/strizhechenko/markov-cli',
    keywords='combinatoric testing utils fuzz pairwise nwise reduce',
    description='Utility designed for check combinations of multiple binary params',
    long_description=(read('README.md')),
    packages=find_packages(exclude=['tests*']),
    scripts=['utils/markov-cli'],
    install_requires=['pymarkovchain'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)

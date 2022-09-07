#!/usr/bin/env python
import os
from setuptools import setup, find_packages

settings = dict()

# TODO: Load dependencies from requirements.txt file

long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

settings.update(
    name='docker-jinja3',
    version='1.0.0',
    description='Extend your dockerfiles with Jinja2 syntax to to more awesome dockerfiles',
    long_description=long_description,
    author='Johan Andersson',
    author_email='Grokzen@gmail.com',
    packages=find_packages(exclude=['.tox', '*test/']),
    scripts=['scripts/dj'],
    install_requires=[
        'PyYAML==6.0',
        'Jinja2==3.1.2',
        'docopt==0.6.2',
    ],
    license="MIT",
    url='https://github.com/Grokzen/docker-jinja',
    classifiers=(
        'Programming Language :: Python :: 3.10',
        'Environment :: Console',
        'Operating System :: POSIX',
    )
)

setup(**settings)

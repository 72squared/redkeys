#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import path
from setuptools import setup
from distutils.cmd import Command


NAME = 'redkeys'

ROOTDIR = path.abspath(os.path.dirname(__file__))

with open(os.path.join(ROOTDIR, 'README.rst')) as f:
    readme = f.read()

with open(os.path.join(ROOTDIR, 'RELEASE.rst')) as f:
    history = f.read()

with open(os.path.join(ROOTDIR, 'redkeys', 'VERSION')) as f:
    version = str(f.read().strip())


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess

        raise SystemExit(
            subprocess.call([sys.executable, '-m', 'test']))


cmdclass = {'test': TestCommand}
ext_modules = []

setup(
    name=NAME,
    version=version,
    description='Redis Keyspace Stats',
    author='John Loehrer',
    author_email='72squared@gmail.com',
    url='https://github.com/72squared/%s' % NAME,
    download_url='https://github.com/72squared/%s/archive/%s.tar.gz' %
                 (NAME, version),
    keywords='redis',
    packages=[NAME],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Environment :: Web Environment',
        'Operating System :: POSIX'],
    license='MIT',
    install_requires=['redis>=2.10.2'],
    tests_require=['redislite>=3.0.287'],
    include_package_data=True,
    long_description=readme + '\n\n' + history,
    cmdclass=cmdclass,
    ext_modules=ext_modules,
    entry_points={'console_scripts': ['redkeys = redkeys.cli:main']}
)

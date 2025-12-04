# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requirements = (
    'pytest',
    'approvaltests',
    'pytest-approvaltests',
    'coverage',
    'autopep8',
    'flake8',
)

setup(
    name='gildedrose',
    python_requires=">3.8,<3.13",
    install_requires=requirements,
    packages=find_packages(),
)

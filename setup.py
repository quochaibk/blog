# -*- coding: utf-8 -*-
"""
    @author: Hai
    @since: Jan 2017
"""

from setuptools import setup, find_packages
import __init__



setup(
    name="blog",
    version=__init__.__version__,
    packages=find_packages(),
    install_requires=['flask>=0.11.1','MySQL-python'],
    author="quochai.kstn@gmail.com"
)

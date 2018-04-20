#!/usr/bin/env python
# -- coding: utf-8 --


"""
install script: python3 setup.py install
"""

from setuptools import setup, find_packages

setup(
    name="KTspider",
    version="2.0.1",
    author="suqi",
    packages=find_packages(exclude=("rules", "config", "spider", "k_test")),
    package_data={
        "": ["*.conf"],         # include all *.conf files
    },
    install_requires=[
        "aiohttp>=1.2.0",       # aiohttp, http for asyncio
        "redis>=2.10.0",        # redis, python client for redis
        "requests>=2.10.0",     # requests, http for humans
    ]
)
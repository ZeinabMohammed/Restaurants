# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in restaurants/__init__.py
from restaurants import __version__ as version

setup(
	name="restaurants",
	version=version,
	description="Restaurants Management",
	author="Github",
	author_email="devzeinab@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

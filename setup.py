#!/usr/bin/env python
import setuptools

setuptools.setup(
    name="python-snowflake",
    version="0.0.1",
    author="Mattonit",
    author_email="itc@matton.it",
    description="Lightweight library to generate unique IDs",
    url="https://github.com/mattonit/python-snowflake",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.2',
)

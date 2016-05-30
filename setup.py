# -*- coding: utf-8 -*-

import sys
import os

from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf-8')

setup(
    name="gotcha",
    version="0.1.0",
    author="teamyy",
    description="A crawler to find a lot of humor post",
    license="MIT",
    keywords="gotcha crawler humor article",
    url="https://github.com/teamyy",
    packages=find_packages(),
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    install_requires=open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().splitlines(),
    classifiers=[  # Ref. https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]
)

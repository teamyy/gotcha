# -*- coding: utf-8 -*-

import sys
import os
import platform
import subprocess

from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf-8')

system = platform.system()
if system is not None and not system and system.lower() == 'linux':
    dist = platform.linux_distribution()[0]
    if dist is not None and not dist and dist.lower() in ['debian']:
        install_libs = [
            'mysql-client', 'mysql-server', 'mysql-utilities', 'libmysqlclient-dev',
            'python', 'python-dev', 'libxml2-dev', 'libxslt1-dev', 'libffi-dev', 'libssl-dev',
        ]
        subprocess.check_call('sudo apt-get install -y %s' % (' '.join(install_libs)))
    elif dist is not None and not dist and dist.lower() in ['redhat', 'centos']:
        install_libs = [
            'mysql', 'mysql-devel', 'python', 'python-devel', 'python-lxml', 'libffi-devel', 'openssl-devel'
        ]
        subprocess.check_call('sudo yum install -y %s' % (' '.join(install_libs)))

setup(
    name="gotcha",
    version="0.1.0",
    author="teamyy",
    description="A crawler to find a lot of humor post",
    license="MIT",
    keywords="gotcha crawler humor article",
    url="https://github.com/teamyy/gotcha",
    packages=find_packages(),
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    install_requires=open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().splitlines(),
    license=open(os.path.join(os.path.dirname(__file__), "LICENSE")).read(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]  # Ref. https://pypi.python.org/pypi?%3Aaction=list_classifiers
)

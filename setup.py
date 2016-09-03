# -*- coding: utf-8 -*-

import sys
import os
import platform
import subprocess

from setuptools import setup, find_packages

reload(sys)
sys.setdefaultencoding('utf-8')

system = platform.system()
if system is not None and system and system.lower() == 'linux':
    dist = platform.linux_distribution()[0]
    if dist is not None and dist and dist.lower() in ['debian']:
        install_libs = [
            'mysql-client', 'mysql-server', 'mysql-utilities', 'libmysqlclient-dev',
            'python', 'python-dev', 'libxml2-dev', 'libxslt1-dev', 'libffi-dev', 'libssl-dev',
            'libtiff4-dev', 'libjpeg8-dev', 'zlib1g-dev', 'libfreetype6-dev' 'liblcms2-dev' 'libwebp-dev', 'tcl8.5-dev', 'tk8.5-dev', 'python-tk', # 이미지 프로세싱에 사용되는 외부 라이브러리
        ]
        subprocess.check_call('sudo apt-get install -y %s' % (' '.join(install_libs)), shell=True)
    elif dist is not None and dist and dist.lower() in ['redhat', 'centos']:
        install_libs = [
            'mysql', 'mysql-devel', 'python', 'python-devel', 'python-lxml', 'libffi-devel', 'openssl-devel',
            'libtiff-devel', 'libjpeg-devel', 'zlib-devel', 'freetype-devel', 'lcms2-devel', 'libwebp-devel', 'tcl-devel', 'tk-devel', # 이미지 프로세싱에 사용되는 외부 라이브러리
        ]
        subprocess.check_call('sudo yum install -y %s' % (' '.join(install_libs)), shell=True)

setup(
    name="gotcha",
    version="0.1.0",
    author="teamyy",
    description="A crawler to find a lot of humor post",
    keywords="gotcha crawler humor article",
    url="https://github.com/teamyy/gotcha",
    packages=find_packages(),
    long_description=open(os.path.join(os.path.dirname(__file__), "README.md")).read(),
    install_requires=open(os.path.join(os.path.dirname(__file__), "requirements.txt")).read().splitlines(),
    license=open(os.path.join(os.path.dirname(__file__), "LICENSE")).read(),
    entry_points={'scrapy': ['settings = gotcha.settings']},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Utilities",
    ]
)

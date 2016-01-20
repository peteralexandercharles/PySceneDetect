#!/usr/bin/env python
#
# PySceneDetect setup.py, based off Glances' setup.py file.
#


import glob
import sys

from setuptools import setup


if sys.version_info < (2, 6) or (3, 0) <= sys.version_info < (3, 3):
    print('PySceneDetect requires at least Python 2.6 or 3.3 to run.')
    sys.exit(1)


def get_data_files():
    data_files = [
        ('share/doc/scenedetect', ['LICENSE', 'LICENSE-NUMPY', 'LICENSE-OPENCV', 'README.md',
                               'docs/changelog.md', 'USAGE.md'])
    ]
    return data_files


def get_requires():
    requires = ['numpy']
    if sys.version_info == (2, 6):
        requires += ['argparse']
    return requires


setup(
    name='PySceneDetect',
    version='0.3.0.1-beta',
    description="A cross-platform, OpenCV-based video scene detection program and Python library. ",
    long_description=open('README.md').read(),
    author='Brandon Castellano',
    author_email='brandon248@gmail.com',
    url='https://github.com/Breakthrough/PySceneDetect',
    license="BSD 2-Clause",
    keywords="video computer-vision analysis",
    install_requires=get_requires(),
    extras_require={
        #'GUI': ['gi'],
        #'VIDEOENC': ['moviepy']
    },
    packages=['scenedetect'],
    include_package_data=True,
    data_files=get_data_files(),
    #test_suite="unitest.py",
    entry_points={"console_scripts": ["scenedetect=scenedetect:main"]},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ]
)
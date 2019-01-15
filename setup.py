#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import girderfs


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    readme = f.read()

classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Filesystems'
]

install_requires = ['fusepy', 'girder-client', 'requests', 'python-dateutil',
                    'six']
if sys.version_info[0] == 2:
    install_requires.append('pathlib')
    install_requires.append('backports.datetime_timestamp')
    install_requires.append('future')

setup(
    name='girderfs',
    version=girderfs.__version__,
    description='FUSE filesystem allowing to mount Girder\'s fs assetstore',
    long_description=readme,
    packages=['girderfs'],
    entry_points={
        'console_scripts': [
            'girderfs = girderfs.__main__:main'
        ]
    },
    install_requires=install_requires,
    tests_require=['pytest'],
    author=girderfs.__author__,
    author_email='xarthisius.kk@gmail.com',
    url='https://github.com/data-exp-lab/girder_fs',
    license='BSD',
    classifiers=classifiers,
)

# -*- coding: utf-8 -*-

import os
import os.path

from setuptools import find_packages
from setuptools import setup

name = 'enchy_admin'
version = '0.0.1'


def find_requires():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    requirements = []
    with open('{0}/requirements.txt'.format(dir_path), 'r') as reqs:
        requirements = reqs.readlines()
    return requirements


if __name__ == "__main__":
    setup(
        name=name,
        version=version,
        description='enchy admin',
        long_description="""enchy admin""",
        classifiers=[
            "Development Status :: 4 - Beta",
            "Programming Language :: Python"
        ],
        packages=find_packages(),
        install_requires=find_requires(),
        data_files=[('enchy_admin', ['enchy_admin/config.yaml'])],
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'enchy = enchy_admin.cli:main'
            ],
        },
    )

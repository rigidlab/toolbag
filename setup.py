from setuptools import setup, find_packages
import os
import sys

setup(
    name='toolbag',
    version='0.1',
    author='rigidlab',
    description='A toolbag for a poly-engineer',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/rigidlab/toolbag',
    python_requires='>=3.6',
    package_dir={'':'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'click',
        'yfinance',
        'pandas',
        'pytubefix'
    ],
    include_package_data=True,
    entry_points = {
        'console_scripts':[
            'toolbag=toolbag.cli:main',
         ]
    }
)
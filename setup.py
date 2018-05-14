"""pypi package setup."""
import codecs
from os import path
from setuptools import setup, find_packages
import ROOT  # pylint: disable=W0611

DEPS = ['numpy', 'PyYAML']

HERE = path.abspath(path.dirname(__file__))

with codecs.open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='hepdata_lib',
    version='0.1.1',
    description='Library for getting your data into HEPData',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/clelange/hepdata_lib',
    author='Andreas Albert, Clemens Lange',
    author_email='clemens.lange@cern.ch',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
    keywords='HEPData physics OpenData',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    zip_safe=False,
    install_requires=DEPS,
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=['pytest', 'pylint'],
    project_urls={
        'Documentation': 'https://hepdata-lib.readthedocs.io',
        'Bug Reports': 'https://github.com/clelange/hepdata_lib/issues',
        'Source': 'https://github.com/clelange/hepdata_lib',
    }, )
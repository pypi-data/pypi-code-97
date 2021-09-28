"""A setuptools based setup module.

Based on https://github.com/pypa/sampleproject.

"""
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    with open(path.join(here, 'HISTORY.rst'), encoding='utf-8') as g:
        long_description = f.read() + '\n\n' + g.read()

setup(
    name='ezi',
    version='0.4.1',
    description=(
        'Interface to the Ezidebit payment gateway for credit card and bank '
        'account payments.'),
    long_description=long_description,
    url='https://github.com/BenSturmfels/python-ezi',
    author='Ben Sturmfels',
    author_email='ben@sturm.com.au',
    license='Apache, Version 2.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=['suds-jurko==0.6'],
    project_urls={
        'Source': 'https://github.com/BenSturmfels/python-ezi',
        'Bug Reports': 'https://github.com/BenSturmfels/python-ezi/issues',
    }
)

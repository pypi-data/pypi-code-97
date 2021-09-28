from itertools import chain
from setuptools import setup, find_packages
from os import path, environ
from time import time

here = path.abspath(path.dirname(__file__))

if path.exists("VERSION.txt"):
    # this file can be written by CI tools (e.g. Travis)
    with open("VERSION.txt") as version_file:
        version = version_file.read().strip().strip("v")
else:
    version = str(time())

req_file_name = 'requirements.min.in'

EXTRAS_REQUIRE = {
    'boto3': ['boto3'],
    'coverage': ['coverage'],
    'awscli': ['awscli'],
    'botocore': ['botocore']
}
EXTRAS_REQUIRE['aws'] = list(set(chain(*EXTRAS_REQUIRE.values())))

with open(req_file_name) as requirements_file:
    install_requires = requirements_file.read().strip().split('\n')

setup(
    name='cco',
    version=version,
    description='''CKAN Cloud Kubernetes operator''',
    url='https://github.com/datopian/ckan-cloud-operator',
    author='''Viderum''',
    license='MIT',
    packages=find_packages(exclude=['examples', 'tests', '.tox']),
    install_requires=install_requires,
    extras_require=EXTRAS_REQUIRE,
    entry_points={
      'console_scripts': [
        'ckan-cloud-operator = ckan_cloud_operator.cli:main',
        'cco = ckan_cloud_operator.cli:main',
      ]
    },
)

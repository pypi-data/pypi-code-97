import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds4n6_lib",
    version="0.6.2",
    author="Jess Garcia",
    author_email="ds4n6@one-esecurity.com",
    description="Bringing Data Science & Artificial Intelligence to the fingertips of the average Forensicator, and promote advances in the field",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ds4n6/ds4n6_lib",
    project_urls={
      "Bug Tracker" : "https://github.com/ds4n6/ds4n6_lib/issues",
      "Website"     : "http://www.ds4n6.io/"
    },
    keywords = ['dfir', 'datascience', 'forensics'],
    install_requires=[
          'requests',
          'numpy',
          'pandas',
          'Evtx',
          'python-evtx',
          'ipyaggrid',
          'IPython',
          'ipywidgets',
          'keras',
          'matplotlib',
          'nbformat',
          'numpy',
          'pandas',
          'pyparsing',
          'qgrid',
          'ruamel.yaml',
          'sklearn',
          'tensorflow',
          'tqdm',
          'traitlets',
          'xmltodict',
      ],
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "Intended Audience :: Information Technology",
      "Framework :: Jupyter",
      "Topic :: Security",
      "Topic :: Scientific/Engineering :: Artificial Intelligence",
      "Topic :: Software Development :: Libraries :: Python Modules",
      "Programming Language :: Python :: 3",
      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)

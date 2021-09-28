import glob
import imp
import setuptools
import sys
import unittest
import os
import shutil

# if version of setuptools is 20.8.1 or below, it doesn't support env specs
if int(setuptools.__version__.split(".")[0]) < 21:
    if sys.version_info[:3] < (3, 5, 0):
        typing_dep = ["typing"]
    else:
        typing_dep = []
else:
    typing_dep = ["typing ; python_version<'3.5.0'"]


def gtirb_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover("tests", pattern="test_*.py")
    return test_suite


# copy over files needed for sdist: README and LICENCE
root_dir = "/builds/rewriting/gtirb"
this_dir = os.path.dirname(__file__)
shutil.copyfile(os.path.join(root_dir, "README.md"), "README")
shutil.copyfile(os.path.join(root_dir, "LICENSE.txt"), "LICENSE")

# Set the version
version = imp.load_source(
    "pkginfo.version", "gtirb/version.py"
).API_VERSION

# run setuptools
if __name__ == "__main__":
    with open("README", "r") as fh:
        long_description = fh.read().replace(
            ".gtirb.svg",
            "https://raw.githubusercontent.com/"
            "GrammaTech/gtirb/master/.gtirb.svg",
        )

    setuptools.setup(
        name="gtirb",
        version=version,
        author="GrammaTech",
        author_email="gtirb@grammatech.com",
        description="GrammaTech Intermediate Representation for Binaries",
        packages=setuptools.find_packages(),
        test_suite="setup.gtirb_test_suite",
        install_requires=["networkx", "protobuf<3.12.2"] + typing_dep,
        classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
        python_requires=">=3",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/grammatech/gtirb",
        license="MIT",
    )

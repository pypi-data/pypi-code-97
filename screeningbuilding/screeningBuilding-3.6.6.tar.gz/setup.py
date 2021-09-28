import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
name="screeningBuilding", # Replace with your own username
version="3.6.6",
author="Dorian Drevon",
author_email="drevondorian@gmail.com",
description="Utilities package",
long_description=long_description,
long_description_content_type="text/markdown",
# url="https://github.com/pypa/sampleproject",
# project_urls={
#     "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
# },
classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
],
packages=['screeningBuilding'],
package_data={'': ['confFiles/*']},
include_package_data=True,
install_requires=['dorianUtilsModulaire==3.8.3','odfpy==1.4.1'],
python_requires=">=3.8"
)

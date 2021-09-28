import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AqEquil",
    version="0.9.1",
    author="Grayson Boyer",
    author_email="gmboyer@asu.edu",
    description="Python tools for aqueous chemical speciation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points={},
    packages=['AqEquil'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['rpy2', 'pandas', 'numpy', 'matplotlib', 'plotly'],
    include_package_data=True,
    package_data={'': ['*.r', '*.min']},
    zip_safe=False
)


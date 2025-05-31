"""
Setup script for CTchargen.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ctchargen",
    version="3.0.0",
    author="Jason McAlpin and Omer Golan-Joel",
    author_email="jason.mcalpin@example.com",
    description="Character generator for Classic Traveller",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/golan2072/CTchargen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    include_package_data=True,
    package_data={
        "ctchargen": [
            "data/*.json",
            "templates/*.template",
            "names/*.txt",
        ],
    },
    entry_points={
        "console_scripts": [
            "ctchargen=src.chargen:main",
        ],
    },
)

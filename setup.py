import os
from pathlib import Path
from setuptools import setup, find_packages

version = [
    line
    for line in Path("sphinx_togglebutton/__init__.py").read_text().split("\n")
    if "__version__" in line
]
version = version[0].split(" = ")[-1].strip('"')

with open("./README.md", "r") as ff:
    readme_text = ff.read()

setup(
    name="sphinx-togglebutton",
    version=version,
    description="Toggle page content and collapse admonitions in Sphinx.",
    long_description=readme_text,
    long_description_content_type="text/markdown",
    author="Chris Holdgraf",
    author_email="choldgraf@berkeley.edu",
    url="https://github.com/executablebooks/sphinx-togglebutton",
    license="MIT License",
    packages=find_packages(),
    package_data={
        "sphinx_togglebutton": ["_static/togglebutton.css_t", "_static/togglebutton.js"]
    },
    install_requires=["setuptools", "wheel", "sphinx", "docutils"],
    extras_require={"sphinx": ["myst_nb", "sphinx_book_theme"]},
    classifiers=["License :: OSI Approved :: MIT License"],
)

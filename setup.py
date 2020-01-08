import os

from setuptools import setup, find_packages
from sphinx_togglebutton import __version__

with open('./README.rst', 'r') as ff:
    readme_text = ff.read()

setup(
    name='sphinx-togglebutton',
    version=__version__,
    description="Add a toggle button to items on a page.",
    long_description=readme_text,
    long_description_content_type='text/x-rst',
    author='Chris Holdgraf',
    author_email='choldgraf@berkeley.edu',
    url="https://github.com/choldgraf/sphinx-togglebutton",
    license='MIT License',
    packages=find_packages(),
    package_data={'sphinx_togglebutton': [
        '_static/togglebutton.css',
        '_static/togglebutton.js'
        ]
    },
    install_requires=["flit", "setuptools", "wheel", "sphinx"],
    classifiers=["License :: OSI Approved :: MIT License"]
)

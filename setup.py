# encoding: utf-8

# ------------------------------------------------------------------------
# Valerio Maggio <@leriomaggio> 2020
# IPython magic function to enable TeXBook Jupyter notebook Theme
# Author: Valerio Maggio <github.com/leriomaggio>
# Code: https://github.com/leriomaggio/texbook-jupyter-theme/
#
# License: Apache License 2.0
# ------------------------------------------------------------------------


import os
from setuptools import setup, find_packages

CURRENT_FOLDER = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURRENT_FOLDER, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="notebook-texbook-theme",
    description=(
        "IPython magic function to dynamically enable the TeXBook"
        "Jupyter Notebook Theme without manually copying resource files in "
        "the default Jupyter custom folder"
    ),
    author="Valerio Maggio",
    author_email="valeriomaggio@gmail.com",
    url="https://github.com/leriomaggio/texbook-jupyter-theme/",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=["notebook", "ipython>=7.0", "jupyter", "jinja2"],
    long_description=long_description,
    long_description_content_type="text/markdown",
)

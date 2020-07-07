# Valerio Maggio <@leriomaggio> 2020
# IPython magic function to enable TeXBook Jupyter notebook Theme
# Author: Valerio Maggio <github.com/leriomaggio>
# Code: https://github.com/leriomaggio/texbook-jupyter-theme/
#
# License: BSD 3 clause

import os
import logging
from setuptools import setup, find_packages
from setuptools.command.install import install
from distutils.cmd import Command


logger = logging.getLogger(__name__)
CURRENT_FOLDER = os.path.abspath(os.path.dirname(__file__))


class ToggleNbServerExtensionCommand(Command):
    """A custom command to enable the TexBook Notebook Server Extension post-install."""

    description = "Toggle TexBook Notebook Server File Handlers extension"

    def initialize_options(self):
        return

    def finalize_options(self):
        return

    def run(self):
        self.announce("Toggle Notebook Server Extension")
        try:
            from notebook.serverextensions import toggle_serverextension_python
        except ImportError:
            logging.warning(
                "notebook must be installed in order to enable server extension"
            )
        else:
            try:
                toggle_serverextension_python(
                    "texbook_theme.nbserver_resource_handler",
                    user=True,
                    sys_prefix=True,
                    enabled=True,
                    logger=logger,
                )
            except ModuleNotFoundError:
                logging.warning(
                    "Could not validate the Extension. Is the module importable?"
                )


class TeXbookThemeInstall(install):
    """Custom Installation command, adding the server extension step."""

    def run(self):
        install.run(self)
        self.run_command("toggle_serverextension")


VERSION = "0.1.1"

with open(os.path.join(CURRENT_FOLDER, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="texbook_theme",
    version=VERSION,
    license=LICENSE,
    description=(
        "IPython magic function to dynamically enable the TeXBook"
        "Jupyter Notebook Theme without manually copying resource files in "
        "the default custom folder"
    ),
    author="Valerio Maggio",
    author_email="valeriomaggio@gmail.com",
    url="https://github.com/leriomaggio/texbook-jupyter-theme/",
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=["notebook", "ipython>=7.0", "jupyter", "jinja2", "tornado"],
    cmdclass={
        "toggle_serverextension": ToggleNbServerExtensionCommand,
        "install": TeXbookThemeInstall,
    },
    entry_points={
        "distutils.commands": [
            "toggle_serverextension = ToggleNbServerExtensionCommand"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)

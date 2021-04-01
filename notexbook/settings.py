# encoding: utf-8

# ------------------------------------------------------------------------
# Valerio Maggio <@leriomaggio> 2020
# IPython magic function to enable TeXBook Jupyter notebook Theme
# Author: Valerio Maggio <github.com/leriomaggio>
# Code: https://github.com/leriomaggio/notexbook-jupyter-theme/
#
# License: Apache License 2.0
# ------------------------------------------------------------------------

from pathlib import Path
import pkg_resources


# -------
# Folders
# -------
TEMPLATES_FOLDER = Path(pkg_resources.resource_filename("notexbook", "templates"))
RESOURCES_FOLDER = Path(pkg_resources.resource_filename("notexbook", "resources"))
EDITOR_THEMES_FOLDER = RESOURCES_FOLDER / "themes"

# Editor Themes
EDITOR_THEMES = {
    "markdown": {
        "material": EDITOR_THEMES_FOLDER / "md_material_theme.css",
        "typora": EDITOR_THEMES_FOLDER / "md_typora_theme.css",
    },
    "code": {
        "material": EDITOR_THEMES_FOLDER / "code_material_theme.css",
        "github": EDITOR_THEMES_FOLDER / "code_github_theme.css",
        "github-light": EDITOR_THEMES_FOLDER / "code_github_light_theme.css",
        "crisp": EDITOR_THEMES_FOLDER / "code_crisp_theme.css",
    },
}

DEFAULT_EDITOR_THEME = "material"
CODE_EDITOR_THEME_CHOICES = list(EDITOR_THEMES["code"].keys())
MD_EDITOR_THEME_CHOICES = list(EDITOR_THEMES["markdown"].keys())

# -------------------
# TeXbook Templates
# -------------------
TEXBOOK_CSS = "noTeXbook_theme_template.jinja2"
TEXBOOK_HTML_TEMPLATE = "noTeXbook_theme.html"

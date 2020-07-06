import os


# -------
# Folders
# -------
BASE_FOLDER = os.path.abspath(os.path.dirname(__file__))
TEMPLATES_FOLDER = os.path.join(BASE_FOLDER, "templates")
RESOURCES_FOLDER = os.path.join(BASE_FOLDER, "resources")
FONTS_FOLDER = os.path.join(RESOURCES_FOLDER, "fonts")
EDITOR_THEMES_FOLDER = os.path.join(RESOURCES_FOLDER, "themes")

#
EDITOR_THEMES = {
    "markdown": {
        "material": os.path.join(EDITOR_THEMES_FOLDER, "md_material_theme.css"),
        "typora": os.path.join(EDITOR_THEMES_FOLDER, "md_typora_theme.css"),
    },
    "code": {
        "material": os.path.join(EDITOR_THEMES_FOLDER, "code_material_theme.css"),
        "github": os.path.join(EDITOR_THEMES_FOLDER, "code_github_theme.css"),
        "crisp": os.path.join(EDITOR_THEMES_FOLDER, "code_crisp_theme.css"),
    },
}

DEFAULT_EDITOR_THEME = "material"
CODE_EDITOR_THEME_CHOICES = list(EDITOR_THEMES["code"].keys())
MD_EDITOR_THEME_CHOICES = list(EDITOR_THEMES["markdown"].keys())

# -------------------
# TeXbook Templates
# -------------------
TEXBOOK_CSS = "texbook_theme_css.jinja2"
TEXBOOK_HTML_TEMPLATE = "texbook_theme.html"

# Resource Fonts URL
TEXBOOK_RESOURCES_FONTS_URL = "/TeXbook_theme/resources/fonts"

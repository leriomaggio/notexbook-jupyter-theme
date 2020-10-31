# encoding: utf-8

# ------------------------------------------------------------------------
# Valerio Maggio <@leriomaggio> 2020
# IPython magic function to enable TeXBook Jupyter notebook Theme
# Author: Valerio Maggio <github.com/leriomaggio>
# Code: https://github.com/leriomaggio/notexbook-jupyter-theme/
#
# License: Apache License 2.0
# ------------------------------------------------------------------------

"""
IPython magic to enable the TeXbook Theme into a Jupyter notebook.

The (line) magic allows for some customisation in the themes to use
for code and markdown editors.
Different themes allow for different colour palettes.
More information on the supported themes, and corresponding
colour palettes can be found here:
https://leriomaggio.github.io/texbook-jupyter-theme/#Code-Editor
"""

from . import settings
from IPython.core.magic import Magics
from IPython.core.magic import magics_class
from IPython.core.magic import line_magic
from IPython.core.magic_arguments import argument
from IPython.core.magic_arguments import magic_arguments
from IPython.core.magic_arguments import parse_argstring
from IPython.core.display import HTML
from jinja2 import FileSystemLoader, Environment
from typing import NamedTuple, Union


# Using typing.NamedTuple rather than @dataclass for broader
# compatibility w/ Py3 versions
class ThemeConfig(NamedTuple):
    code_theme_name: str
    md_theme_name: str
    code_mono_font: str
    code_mono_font_size: str
    md_mono_font: str
    md_mono_font_size: str
    nb_font_size: str
    nb_line_height: Union[str, float]

    @staticmethod
    def normalise_fontsize(value):
        if not value.endswith("px"):
            return f"{value.strip()}px"
        return value.strip()

    def as_dict(self):
        fs = self.__class__.__dict__["_fields"]
        return {k: v for k, v in zip(fs, map(lambda f: getattr(self, f, ""), fs))}


def create_config_from(args) -> ThemeConfig:
    """factory method from command line arguments"""
    code_theme, md_theme = args.code_theme, args.md_theme
    code_mono_font, code_mono_font_size = (
        args.code_mono_font,
        args.code_mono_font_size,
    )
    md_mono_font, md_mono_font_size = args.md_mono_font, args.md_mono_font_size
    nb_font_size, nb_line_height = args.nb_font_size, args.nb_line_height

    code_mono_font_size = ThemeConfig.normalise_fontsize(code_mono_font_size)
    md_mono_font_size = ThemeConfig.normalise_fontsize(md_mono_font_size)
    nb_font_size = ThemeConfig.normalise_fontsize(nb_font_size)

    return ThemeConfig(
        code_theme_name=code_theme,
        md_theme_name=md_theme,
        code_mono_font=code_mono_font,
        code_mono_font_size=code_mono_font_size,
        md_mono_font=md_mono_font,
        md_mono_font_size=md_mono_font_size,
        nb_line_height=nb_line_height,
        nb_font_size=nb_font_size,
    )


@magics_class
class TeXbookTheme(Magics):
    """
    IPython (line) magic to enable the TeXbook theme
    in a Jupyter notebook.

    The magic allows for some customisation in the
    themes used for code and markdown editors
    (default theme: Material Design Light theme).

    For information: `%texify?`
    """

    def __init__(self, *args, **kwargs):
        super(TeXbookTheme, self).__init__(*args, **kwargs)
        template_loader = FileSystemLoader(
            [settings.TEMPLATES_FOLDER, settings.RESOURCES_FOLDER]
        )
        self.template_env = Environment(loader=template_loader)

    @magic_arguments()
    @argument(
        "-cdth",
        "--code-theme",
        type=str,
        choices=settings.CODE_EDITOR_THEME_CHOICES,
        help="Colour Theme for Code Editor",
        default=settings.DEFAULT_EDITOR_THEME,
        dest="code_theme",
    )
    @argument(
        "-mdth",
        "--md-theme",
        choices=settings.MD_EDITOR_THEME_CHOICES,
        help="Colour Theme for Markdown Editor",
        default=settings.DEFAULT_EDITOR_THEME,
        dest="md_theme",
    )
    @argument(
        "-cdf",
        "--code-font",
        help="Font family used in Code Editor. Default: Fira Code",
        default="Fira Code",
        dest="code_mono_font",
    )
    @argument(
        "-mdf",
        "--md-font",
        help="Font family used in Markdown Editor. Default: Hack",
        default="Hack",
        dest="md_mono_font",
    )
    @argument(
        "-cdfs",
        "--code-fontsize",
        help="Font size used in Code and Markdown Editor. Default: 16px",
        default="16px",
        dest="code_mono_font_size",
    )
    @argument(
        "-mdfs",
        "--md-fontsize",
        help="Font size of Rendered Markdown monospace. Default: 16px",
        default="16px",
        dest="md_mono_font_size",
    )
    @argument(
        "-nbfs",
        "--notebook-font-size",
        help="Font size of Rendered Content in Notebook. Default: 19px",
        default="19px",
        dest="nb_font_size",
    )
    @argument(
        "-lh",
        "--linespread",
        help="Line height of Notebook Content. Default: 1.4",
        default="1.4",
        dest="nb_line_height",
    )
    @line_magic
    def texify(self, line):
        """
        IPython magic function to trigger the activation
        of the TeXBook-Jupyter theme in the notebook.
        """
        args = parse_argstring(self.texify, line)
        config = create_config_from(args)
        theme_css = self._load_texbook_theme_template(config)
        template = self.template_env.get_template(settings.TEXBOOK_HTML_TEMPLATE)
        theme_style_tag = template.render(textbook_css=theme_css)

        return HTML(theme_style_tag)

    def _load_texbook_theme_template(self, config: ThemeConfig):
        md_theme_css = settings.EDITOR_THEMES["markdown"][config.md_theme_name]
        cd_theme_css = settings.EDITOR_THEMES["code"][config.code_theme_name]

        with open(md_theme_css) as md_theme_file, open(cd_theme_css) as cd_theme_file:
            md_theme = md_theme_file.read()
            code_theme = cd_theme_file.read()
            t = self.template_env.get_template(settings.TEXBOOK_CSS)
            return t.render(
                code_theme=code_theme, md_theme=md_theme, **config.as_dict()
            )


def load_ipython_extension(ipython):
    ipython.register_magics(TeXbookTheme)

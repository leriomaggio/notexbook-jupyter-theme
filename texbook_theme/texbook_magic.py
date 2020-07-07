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


@magics_class
class TeXBookTheme(Magics):
    """
    IPython (line) magic to enable the TeXbook theme
    in a Jupyter notebook.

    The magic allows for some customisation in the
    themes used for code and markdown editors
    (default theme: Material Design Light theme).

    For information:
    `%TeXbook_theme?`
    """

    def __init__(self, *args, **kwargs):
        super(TeXBookTheme, self).__init__(*args, **kwargs)
        template_loader = FileSystemLoader(
            [settings.TEMPLATES_FOLDER, settings.RESOURCES_FOLDER]
        )
        self.template_env = Environment(loader=template_loader)

    @magic_arguments()
    @argument(
        "-ct",
        "--code-theme",
        type=str,
        choices=settings.CODE_EDITOR_THEME_CHOICES,
        help="Code Editor Theme",
        default=settings.DEFAULT_EDITOR_THEME,
        dest="code_theme",
    )
    @argument(
        "-mt",
        "--md-theme",
        choices=settings.MD_EDITOR_THEME_CHOICES,
        help="Markdown Editor Theme",
        default=settings.DEFAULT_EDITOR_THEME,
        dest="md_theme",
    )
    @line_magic
    def TeXbook_theme(self, line):
        """
        IPython magic function to trigger the activation
        of the TeXBook-Jupyter theme in the notebook.
        """
        args = parse_argstring(self.texbook_theme, line)
        code_theme, md_theme = args.code_theme, args.md_theme
        theme_css = self._load_TeXbook_template(
            code_theme_name=code_theme, md_theme_name=md_theme
        )
        template = self.template_env.get_template(settings.TEXBOOK_HTML_TEMPLATE)
        theme_style_tag = template.render(textbook_css=theme_css)

        return HTML(theme_style_tag)

    def _load_TeXbook_template(self, code_theme_name, md_theme_name):
        md_theme_css = settings.EDITOR_THEMES["markdown"][md_theme_name]
        cd_theme_css = settings.EDITOR_THEMES["code"][code_theme_name]

        with open(md_theme_css) as md_theme_file, open(cd_theme_css) as cd_theme_file:
            md_theme = md_theme_file.read()
            cd_theme = cd_theme_file.read()
            t = self.template_env.get_template(settings.TEXBOOK_CSS)
            return t.render(
                fonts_path=settings.TEXBOOK_RESOURCES_FONTS_URL,
                code_theme=cd_theme,
                md_theme=md_theme,
            )


def load_ipython_extension(ipython):
    ipython.register_magics(TeXBookTheme)

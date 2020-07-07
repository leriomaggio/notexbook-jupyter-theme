# encoding: utf-8

# ------------------------------------------------------------------------
# Valerio Maggio <@leriomaggio> 2020
# IPython magic function to enable TeXBook Jupyter notebook Theme
# Author: Valerio Maggio <github.com/leriomaggio>
# Code: https://github.com/leriomaggio/texbook-jupyter-theme/
#
# License: Apache License 2.0
# ------------------------------------------------------------------------

"""
Jupyter notebook server extension to allow serving custom
static (font) files from notebook.

The extension uses a (default) Tornado `StaticFileHandler`
mapped to CSS resource folder.

This extension will be automatically installed
as a part of the post-install behaviour.
"""

from tornado.web import StaticFileHandler
from . import settings


def load_jupyter_server_extension(nb_server_app):
    web_app = nb_server_app.web_app
    host_pattern = ".*$"
    web_app.add_handlers(
        host_pattern,
        [
            (
                r"{}/(.*)".format(settings.TEXBOOK_RESOURCES_FONTS_URL),
                StaticFileHandler,
                {"path": settings.FONTS_FOLDER},
            )
        ],
    )

# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/stable/config

import os
import shutil
from datetime import datetime

from pkg_resources import get_distribution

# import sphinx_fontawesome


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#


# -- Project information -----------------------------------------------------

project = "s2-ws-json-python"
copyright = f"{datetime.now().year}, TNO and Seita..."
author = "TNO B.V. and Seita"

# The full version, including alpha/beta/rc tags
release = get_distribution("s2-ws-json-python").version
# The short X.Y.Z version
version = ".".join(release.split(".")[:3])

# rst_prolog = sphinx_fontawesome.prolog

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# # ones.
extensions = [
    "sphinx_rtd_theme",
    "sphinx.ext.intersphinx",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.todo",
    "sphinx_copybutton",
    "sphinx_tabs.tabs",
    "sphinx_fontawesome",
    "sphinxcontrib.autohttp.flask",
    "sphinxcontrib.autohttp.flaskqref",
    "sphinx.ext.autosummary",
    "sphinx.ext.autodoc.typehints",
    "sphinx.ext.autodoc",
]

autodoc_typehints = "signature"


autodoc_default_options = {
    "member-order": "bysource",
}

# autodoc_default_options = {}

# # Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# # if GEN_CODE_DOCS is not found, the default is gen_code_docs=True
# gen_code_docs = not bool(
#     os.environ.get("GEN_CODE_DOCS", "True").lower() in ("f", "false", "0")
# )


# # Generate code docs
# if gen_code_docs:

#     # Add dependencies
#     extensions.extend(
#         [
#             "sphinx.ext.autosummary",
#             "sphinx.ext.autodoc.typehints",
#             "sphinx.ext.autodoc",
#         ]
#     )
# else:
#     if os.path.exists("_autosummary"):
#         shutil.rmtree("_autosummary")

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "_templates"]

# Todo: these are not mature enough yet for release, or should be removed
# exclude_patterns.append("int/*.rst")
# exclude_patterns.append("concepts/assets.rst")
# exclude_patterns.append("concepts/markets.rst")
# exclude_patterns.append("concepts/users.rst")
# exclude_patterns.append("api/aggregator.rst")
# exclude_patterns.append("api/mdc.rst")
# exclude_patterns.append("api/prosumer.rst")
# exclude_patterns.append("api/supplier.rst")

# Whether to show todo notes in the documentation
todo_include_todos = True

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# html_logo = "https://artwork.lfenergy.org/projects/flexmeasures/horizontal/white/flexmeasures-horizontal-white.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# #
# html_theme_options = {
#     "logo_only": True,
# }

# html_theme_options = {
#     'navigation_depth': 4,
# }

# Add any paths that contain custom _static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin _static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
# html_css_files = ["css/custom.css"]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "S2WSJSONdoc"


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------


# -- Options for copybytton extension ---------------------------------------
copybutton_prompt_is_regexp = True
copybutton_prompt_text = r">>> |\.\.\. |\$ "  # Python Repl + continuation + Bash
copybutton_line_continuation_character = "\\"

# -- Options for ifconfig extension ---------------------------------------


def setup(sphinx_app):
    pass

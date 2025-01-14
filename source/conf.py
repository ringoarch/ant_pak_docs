# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme
import os
import sys


sys.path.insert(
    0,
    os.path.abspath("../.."),
)
# sys.path.insert(
#     0,
#     os.path.abspath(
#         "C:\\Users\\ringo\\AppData\\Roaming\\McNeel\\Rhinoceros\\7.0\\Plug-ins\\IronPython (814d908a-e25c-493d-97e9-ee3861957f49)\\settings\\lib"
#     ),
# )
# sys.path.insert(
#     0,
#     os.path.abspath("C:\\Program Files\\ladybug_tools\\python\\Lib\\site-packages"),
# )

# sys.path.insert(
#     0,
#     os.path.abspath("C:\\Program Files\\Rhino 7\\Plug-ins\\IronPython\\Lib"),
# )

# print(sys.path)
project = "Ant pak"
copyright = "2025, ringo"
author = "ringo"
release = "0.1.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.imgmath",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    # "sphinxcontrib.fulltoc",
    "sphinx.ext.napoleon",
    # "sphinx_click.ext",
]

autodoc_mock_imports = [
    "Rhino",
    "scriptcontext",
    "ghpythonlib",
    "rhinoscriptsyntax",
    "System",
    "Grasshopper",
    "gh",
    "ant_pak.setup",
    # "ant_pak",
]

templates_path = ["_templates"]
exclude_patterns = []

# source_suffix = ".rst"


language = "zh"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
html_static_path = ["_static"]
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

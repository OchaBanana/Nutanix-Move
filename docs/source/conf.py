# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nutanix Move'
copyright = '2022, Nutanix'
author = 'Toh'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# import sphinx_rtd_theme
# html_theme = 'sphinx_rtd_theme'
import sphinx_bootstrap_theme
import sphinx_fontawesome
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()
#html_static_path = ['_static']
extensions = ['sphinx.ext.todo',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.fulltoc',
    'sphinx_fontawesome']

html_logo = "_static/NutanixWorkshops.svg"

html_favicon = "_static/favicon.ico"

html_title = ""

html_show_sphinx = False
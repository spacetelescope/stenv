# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
from datetime import datetime

import dunamai
import packaging.version
import sphinx


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information


project = 'Space Telescope Environment (`stenv`)'
author = 'Space Telescope Science Institute'
copyright = f'{datetime.today().year}, {author}'
release = dunamai.Version.from_any_vcs('(?P<base>\d+\.\d+\.\d+)').serialize()
version = release.split('-', 1)[0]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'


def check_sphinx_version(expected_version):
    installed_version = packaging.version.Version(sphinx.__version__)
    expected_version = packaging.version.Version(expected_version)
    if installed_version < expected_version:
        raise RuntimeError(
            f"At least Sphinx version {expected_version} is required to build this documentation. "
            f"Found {installed_version}."
        )


intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
}

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx_inline_tabs',
]

templates_path = ['_templates']
exclude_patterns = []

# Enable nitpicky mode - which ensures that all references in the docs resolve.
nitpicky = False
nitpick_ignore = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []

html_theme_options = {
    "collapse_navigation": True
    # "nosidebar": "false",
    # "sidebarbgcolor": "#4db8ff",
    # "sidebartextcolor": "black",
    # "sidebarlinkcolor": "black",
    # "headbgcolor": "white",
}

# The name for this set of Sphinx documents. If None, it defaults to "<project> v<release> documentation".
html_title = f'{project} v{release} documentation'

# A shorter title for the navigation bar. Default is the same as html_title.
html_short_title = html_title

# The name of an image file (within the static path) to use as favicon of the docs.
# This file should be a Windows icon file (.ico) being 16x16 or 32x32 pixels large.
html_favicon = None

# Add any extra paths that contain custom files (such as robots.txt or .htaccess) here, relative to this directory.
# These files are copied directly to the root of the documentation.
html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom, using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to typographically correct entities.
html_use_smartypants = False

# Custom sidebar templates, maps document names to template names.
html_sidebars = {'**': ['globaltoc.html', 'relations.html', 'searchbox.html']}

# Additional templates that should be rendered to pages, maps page names to template names.
html_additional_pages = {}

# If false, no module index is generated.
html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will contain a <link> tag referring to it.
# The value of this option must be the base URL from which the finished HTML is served.
html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = project

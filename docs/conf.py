"""Build user documentation for the installed starter package."""

from importlib.metadata import version as _package_version

project = "TODO: Python project"
author = "TODO: Responsible team"
release = _package_version("todo-python-project")
version = release
extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "myst_parser"]
exclude_patterns = ["_build"]
html_theme = "alabaster"
html_show_copyright = False

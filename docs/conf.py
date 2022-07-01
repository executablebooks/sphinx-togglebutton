# -- Project information -----------------------------------------------------

project = "Sphinx Toggle Button"
copyright = "2018, Chris Holdgraf"
author = "Chris Holdgraf"

# The short X.Y version
version = ""
# The full version, including alpha/beta/rc tags
release = ""


# -- General configuration ---------------------------------------------------
extensions = ["myst_nb", "sphinx_examples", "sphinx_design", "sphinx_togglebutton"]
templates_path = ["_templates"]
source_suffix = ".rst"
main_doc = "index"
language = None
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------
html_theme = "sphinx_book_theme"
# html_theme = "sphinx_rtd_theme"  # These are just for testing
# html_theme = "alabaster"
# html_theme = "furo"

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/sphinx-togglebutton",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "home_page_in_toc": True,
}

myst_enable_extensions = ["colon_fence"]

# To test behavior in JS
# togglebutton_hint = "test show"
# togglebutton_hint_hide = "test hide"
# togglebutton_open_on_print = False

"""A small sphinx extension to add "toggle" buttons to items."""
import os

__version__ = "0.0.3dev0"


def st_static_path(app):
    static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "_static"))
    app.config.html_static_path.append(static_path)


# This function reads in a variable and inserts it into JavaScript
def insert_custom_selection_config(app):
    # This is a configuration that you've specified for users in `conf.py`
    selector = app.config["togglebutton_selector"]
    js_text = "var togglebuttonSelector = '%s';" % selector
    app.add_js_file(None, body=js_text)


# We connect this function to the step after the builder is initialized
def setup(app):
    # Add our static path
    app.connect("builder-inited", st_static_path)

    # Add relevant code to headers
    app.add_stylesheet("togglebutton.css")

    # Add the string we'll use to select items in the JS
    # Tell Sphinx about this configuration variable
    app.add_config_value("togglebutton_selector", ".toggle", "html")
    app.add_js_file("togglebutton.js")

    # Run the function after the builder is initialized
    app.connect("builder-inited", insert_custom_selection_config)

    return {
        "version": __version__,
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

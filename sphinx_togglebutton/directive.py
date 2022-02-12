import email
from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective


class ToggleAllInGroupNode(nodes.Element):
    """Appended to the doctree by the ToggleAll directive

    Renders as a button to enable thebe on the page.

    If no ToggleAll directive is found in the document but thebe
    is enabled, the node is added at the bottom of the document.
    """

    def __init__(self, rawsource="", *children, group=None, text="Toggle All", **attributes):
        super().__init__("", text=text, group=group)

    def html(self):
        text = self["text"]
        group = self["group"]
        return (f"""\
              <button title="{text}"
               class="toggle-all-button toggle-button-style"
               onclick="toggleAllByGroup('{group}')"
              >{text}</button>""")


class ToggleAllInGroupButton(SphinxDirective):
    """Trigger toggle on all elements that match a group."""

    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
      "text": directives.unchanged
    }
    has_content = False

    def run(self):
        kwargs = {}
        if self.arguments:
            kwargs["group"] = self.arguments[0]
        else:
            kwargs["group"] = "**"

        if self.options.get("text"):
            kwargs["text"] = self.options["text"]
        else:
            if kwargs["group"] == "**":
                msg = "Toggle all content"
            else:
                msg = f"Toggle all {kwargs['group']}"
            kwargs["text"] = msg
        return [ToggleAllInGroupNode(**kwargs)]


class Toggle(SphinxDirective):
    """Hide a block of markup text by wrapping it in a container."""

    optional_arguments = 1
    final_argument_whitespace = True
    has_content = True

    option_spec = {"id": directives.unchanged, "show": directives.flag}

    def run(self):
        self.assert_has_content()
        classes = ["toggle"]
        if "show" in self.options:
            classes.append("toggle-shown")

        parent = nodes.container(classes=classes)
        self.state.nested_parse(self.content, self.content_offset, parent)
        return [parent]

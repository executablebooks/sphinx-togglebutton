# `sphinx-togglebutton`

A small sphinx extension to add "toggle button" elements to sections of your page.
This allows you to:

- Collapse admonitions (notes, warnings, etc) so that their content is hidden
  until users click a toggle button. See {ref}`dropdown-admonitions`.
- Collapse arbitrary chunks of content on your page with a `toggle` directive.
  See {ref}`toggle-directive`.

:::{admonition} For example, click the "+" button to the right:
:class: dropdown

Here's a toggled note! You can put all kinds of stuff in here!
:::

You can also add a toggle button to arbitrary chunks of content.
For example, click the toggle button to the right just below.

::::{toggle}
:::{admonition} Wow!
:class: tip

It's a code block!

```python
a = "wow, very python"
```
:::
::::

See {ref}`usage` for more information.

:::{admonition} Check out sphinx-panels as well!
:class: tip

For a bootstrap-based "dropdown" directive that uses pure CSS, check out
[Sphinx Panels](https://sphinx-panels.readthedocs.io/en/latest/#dropdown-usage)
:::

```{toctree}
use
reference/index
```

## Installation

You can install `sphinx-togglebutton` with `pip`:

```bash
pip install sphinx-togglebutton
```

Then, activate it in your `sphinx` build by adding it to your `conf.py` configuration
file, like so:

E.g.:

```python
extensions = [
    ...
    'sphinx_togglebutton'
    ...
]
```

See {ref}`usage` for information about how to use `sphinx-togglebutton`.

# `sphinx-togglebutton`

A small sphinx extension to add "toggle button" elements to sections of your page.
For example:

## Collapse admonitions

You can collapse admonitions (notes, warnings, etc) so that their content is hidden until users click the admonition title.

````{example}
:::{admonition} Click the title to toggle
:class: dropdown

This title was made into a dropdown admonition by adding `:class: dropdown` to it.
:::
````

See {ref}`dropdown-admonitions` for more information.

## Hide any content behind a toggle button

You can also hide arbitrary content behind a toggle button.
When users press the button, they will see the content.
For example:

````{example}
```{toggle}
This is a toggled content block!
```
````

You can either do this with a `{toggle}` directive, or by adding a `toggle` CSS class to any elements you'd like hidden behind a toggle button.

See [](use:css-selector) for more details.

:::{admonition} Check out sphinx-design as well!
:class: tip

For a bootstrap-based "dropdown" directive that uses pure CSS, check out
[Sphinx Design](https://sphinx-design.readthedocs.io/en/latest/dropdowns.html)
:::

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


```{toctree}
:maxdepth: 2
use
reference/index
changelog
```
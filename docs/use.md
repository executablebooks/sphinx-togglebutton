(usage)=
# Use and configure

This page covers how to use and configure / customize `sphinx-togglebutton`.

There are two main ways to use `sphinx-togglebutton`:

- Collapse admonitions with the `dropdown` class
- Make arbitrary chunks of content "toggle-able" with the `toggle` directive

Both are described below

(dropdown-admonitions)=
## Collapse admonitions with the `dropdown` class

Making dropdown admonitions allows you to insert extra information in your document
without forcing the user to see that content. For example:

:::{admonition} What could be inside this warning?
:class: warning, dropdown

A whale of a joke!

```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
```
:::

Create a dropdown admonition by adding the `dropdown` class to an admonition directive.
For example, like so:

::::{tab-set}

:::{tab-item} MyST

````md

```{note}
:class: dropdown

My note
```
````

:::

:::{tab-item} reStructuredText

```rst
.. note::
   :class: dropdown

   My note
```

:::
::::

You can use a custom admonition title and apply the style of a "built-in"
admonition (e.g., `note`, `warning`, etc) with the `admonition::` directive:

::::{tab-set}

:::{tab-item} MyST

````md
```{admonition} Here's my title
:class: dropdown, warning

My note
```
````

:::

:::{tab-item} reStructuredText

```rst
.. admonition:: Here's my title
   :class: dropdown, warning

   My note
```

:::
::::

Creates:

:::{admonition} Here's my title
:class: dropdown, warning

My custom admonition!
:::

To show the content by default, add a `toggle-shown` class as well.

:::{tab-set-code}

````markdown
```{note}
:class: dropdown, toggle-shown

This is my note.
```
````

```rst
.. note::
    :class: dropdown, toggle-shown

    This is my note.
```

:::

This will generate the following block:

:::{note}
:class: dropdown, toggle-shown

This is my note.
:::

(toggle-directive)=
## Toggle any content with the toggle directive

To add toggle-able content, use the **toggle directive**. This directive
will wrap its content in a toggle-able container. You can call it like so:

:::{tab-set-code}

````markdown
```{toggle}
Here is my toggle-able content!
```
````

```rst
.. toggle::

   Here is my toggle-able content!
```

:::


The code above results in:

:::{toggle}

Here is my toggle-able content!
:::

To show the toggle-able content by default, use the `:show:` flag.

````markdown
```{toggle}
:show:

Here is my toggle-able content!
```
````

It results in the following:

:::{toggle}
:show:

Here is my toggle-able content!
:::

## Control the togglebutton hover text

You can control the "hint" text that is displayed next to togglebuttons when
their content is collapsed. To do so, use the following configuration variable
in your `conf.py` file:

```python
togglebutton_hint = "My text"
```

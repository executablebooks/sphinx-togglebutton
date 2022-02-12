# Reference examples

This page shows the most common ways that `sphinx-togglebutton` is used as a reference.
This is a benchmark for styling, and also helps demonstrate the behavior of this extension.

## Toggle all button

Here's a button that will toggle all items of a particular type

```{toggle-all-button}
```

With a custom title:

```{toggle-all-button} A test!
```

## Use amongst text

Here's a paragraph, it's just here to provide some text context for the togglebuttons in this section.

:::{note}
:class: toggle

A test toggle admonition.
:::

Here's a paragraph, it's just here to provide some text context for the togglebuttons in this section.

:::{toggle}
A test toggle directive.
:::


Here's a paragraph, it's just here to provide some text context for the togglebuttons in this section.


## Sequential toggle buttons

Here's how they look right after one another:

### Admonition toggles

:::{note}
:class: toggle

This is my note.
:::

:::{note}
:class: toggle

This is my second.
:::

### Toggle directive

:::{toggle}
This is my first.
:::

:::{toggle}
This is my second.
:::

## Long titles

:::{admonition} A really long admonition that will take up multiple lines A really long admonition that will take up multiple lines
:class: toggle

Admonition content.

```{image} https://jupyterbook.org/_static/logo-wide.svg
```
:::

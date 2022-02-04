---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Reference examples

This page shows the most common ways that `sphinx-togglebutton` is used as a reference.
This is a benchmark for styling, and also helps demonstrate the behavior of this extension.

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

## MyST-NB Cells

```{code-cell}
from matplotlib import pyplot as plt
import numpy as np
data = np.random.randn(3, 100)
```

### Hide Input

```{code-cell}
:tags: [hide-input]

fig, ax = plt.subplots()
ax.scatter(data[0], data[1], c=np.abs(data[2]))
```

### Hide Output

```{code-cell}
:tags: [hide-output]

fig, ax = plt.subplots()
ax.scatter(data[0], data[1], c=np.abs(data[2]))
```

### Hide Both

```{code-cell}
:tags: [hide-cell]

fig, ax = plt.subplots()
ax.scatter(data[0], data[1], c=np.abs(data[2]))
```

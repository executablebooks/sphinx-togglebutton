---
jupytext:
  cell_metadata_filter: -all
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

# MyST Notebooks

`sphinx-togglebutton` is particularly useful with `MyST-NB` notebooks.
This is used to show and hide code cell inputs and outputs.

Here is a demonstration of the functionality.

## `{toggle-all-button}` usage

The code below generated the buttons that follow:

````
```{toggle-all-button}
```

```{toggle-all-button} Toggle all inputs
:selector: .cell.tag_hide-input .cell_input
```

```{toggle-all-button} Toggle all outputs
:selector: .cell.tag_hide-output .cell_output
```
````

```{toggle-all-button}
```

```{toggle-all-button} Toggle all inputs
:selector: .cell.tag_hide-input .cell_input
```

```{toggle-all-button} Toggle all outputs
:selector: .cell.tag_hide-output .cell_output
```

## Cell inputs

```{code-cell}
:tags: [hide-input]
for ii in range(20):
  print(f"Number: {ii}")
```

## Cell outputs

```{code-cell}
:tags: [hide-output]
for ii in range(20):
  print(f"Number: {ii}")
```

## Hide the whole cell

```{code-cell}
:tags: [hide-cell]
for ii in range(20):
  print(f"Number: {ii}")
```

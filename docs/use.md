(usage)=
# Use and configure

This page covers how to use and configure / customize `sphinx-togglebutton`.

There are three main ways to use `sphinx-togglebutton`:

- Wrap arbitrary objects in a toggle button via a CSS selector
- Collapse admonitions with the `dropdown` class
- Make arbitrary chunks of content "toggle-able" with the `toggle` directive

Each is described below

(use:css-selector)=
## Collapse a block of content with a CSS selector

You can hide any content and display a toggle button to show it by using certain CSS classes.
`sphinx-togglebutton` will wrap elements with these classes in a `<details>` block like so:

```html
<details>
  <summary>Click to show</summary>
  <!-- Element that had a CSS class selector -->
</details>
```

:::{admonition} example
:class: tip
This MyST Markdown:

````md
```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
:class: toggle
```
````
results in:
```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
:class: toggle
```
:::

### Configure the CSS selector used to insert toggle buttons

By default, `sphinx-togglebutton` will use this selector:

```
.toggle, .admonition.dropdown
```

However, you can customize this behavior with the `togglebutton_selector` configuration value.
To specify the selector to use, pass a valid CSS selector as a string:

:::{admonition} example
:class: tip
Configure `sphinx-togglebutton` to look for a `.toggle-this-element` class and an element with ID `#my-special-id` **instead of** `.toggle` and `.admonition.dropdown`.

```python
sphinx_togglebutton_selector = ".toggle-this-element, #my-special-id"
```
:::

(dropdown-admonitions)=
## Collapse admonitions with the `dropdown` class

`sphinx-togglebutton` treats admonitions as a special case if they are selected.
If a Sphinx admonition matches the toggle button selector, then its title will be displayed with a button to reveal its content.

:::{admonition} example
:class: tip
````md
```{admonition} This will be shown
:class: dropdown
And this will be hidden!
```
````
results in 
```{admonition} This will be shown
:class: dropdown
And this will be hidden!
```
:::

This works for any kind of Sphinx admoniton:

:::{note}
:class: dropdown
A note!
:::

:::{warning}
:class: dropdown
A warning!
:::


(toggle-directive)=
## Use the `{toggle}` directive to toggle blocks of content

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

## Change the button hint text

You can control the "hint" text that is displayed next to togglebuttons.
To do so, use the following configuration variable in your `conf.py` file:

```python
togglebutton_hint = "Displayed when the toggle is closed."
togglebutton_hint_hide = "Displayed when the toggle is open."
```

## Change the toggle icon color

You can apply some extra styles to the toggle button to achieve the look you want.
This is particularly useful if the color of the toggle button does not contrast with the background of an admonition.

To style the toggle button, [add a custom CSS file to your documentation](https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html) and include a custom CSS selector like so:

```scss
// Turn the color red...
// ...with admonition toggle buttons
button.toggle-button {
  color: red;
}

// ...with content block toggle buttons
.toggle-button summary {
  color: red;
}
```
(usage)=
# Use and configure

This page covers how to use and configure / customize `sphinx-togglebutton`.

**To toggle content**, there are two options:

- Use [a CSS selector](use:css-selector) to identify and toggle content
- Use [a `{toggle}` directive](use:toggle-directive) to toggle chunks of content.

**To toggle multiple items at once** you may **group** elements to toggle, and [insert a button to toggle all items of a group](use:toggle-groups).

Each is described below.

(use:css-selector)=
## Collapse content with a toggle button

You can hide any content and display a toggle button to show it.
There are two ways to do this.

### With CSS classes

`sphinx-togglebutton` will use a CSS selector to match elements on a page, and will convert each of them into toggle-able content.
By default, `sphinx-togglebutton` uses this selector:

```
.toggle, .admonition.dropdown
```

This will match any items with `toggle` class, and Sphinx admonitions with a `dropdown` class.

:::{example} A div with a `toggle` class 
Create a `div` with a `toggle` class, so that `sphinx-togglebutton` will detect it with the default selector:

````
```{container} toggle
Some toggled content with a `toggle` class.
```
````

results in:

```{container} toggle
Some toggled content with a `toggle` class.
```
:::

:::{tip}
You can change the selector that is used by providing your own selector in `togglebutton_selector`.
However, a more flexible way to control which elements are toggled is [to use toggle button groups](use:toggle-groups).
:::

(use:toggle-directive)=
### With the `{toggle}` directive

As a short-hand for the above approach, there is a `{toggle}` directive to quickly wrap content in a Toggle button.
The content of the `{toggle}` directive will be wrapped in a `<details>` element (see [](use:block-level)).

:::{example} Wrap an image with a `{toggle}` directive
To wrap an image use the toggle directive like so:

````
```{toggle}
Here is my toggle-able content!
```
````
results in

```{toggle}
Here is my toggle-able content!
```
:::

#### Show the content by default

To show the toggle-able content by default, use the `:show:` flag.

:::{example} Show content by default

````
```{toggle}
:show:
Here is my toggle-able content!
```
````

results in

```{toggle}
:show:
Here is my toggle-able content!
```
:::

## Types of toggled content

There are two types of toggle-able content: [block-level toggles](use:block-level) and [admonition toggles](use:admonition-toggle).

(use:block-level)=
### Block-level toggles

For most content, `sphinx-togglebutton` will wrap elements that match the selector in a `<details>` block.
The block looks like this:

```{toggle}
Some toggle-able content!
```

These blocks have the following `<details>` structure:

```html
<details>
  <summary>Click to show</summary>
  <!-- Element that had a CSS class selector -->
</details>
```

:::{example} Block-level toggles
Add a `toggle` class to an image directive so that it becomes toggled.

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


(use:admonition-toggles)=
### Admonition toggles

If the matched element **also has an `admonition` class** then `sphinx-togglebutton` will treat it as a Sphinx admonition, and will only toggle the _content_ of the admonition.
For example:

:::{warning}
:class: dropdown
A toggled warning!
:::

The default selector will match admonitions with a `dropdown` class (the selector is `.admonitions.dropdown`).

:::{example} Make an `{admonition}` toggled

Create a toggled admonition by adding the `dropdown` class to it.

`````md
````{admonition} Here's my admonition
:class: dropdown

```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
```
````
`````

results in:

````{admonition} Here's my admonition
:class: dropdown

```{image} https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif
```
````
:::


(use:toggle-groups)=
## Create groups of toggled content

You can create groups of toggle content that can each be opened and closed as a group.
To do so, use the `togglebutton_groups` configuration.
This is a dictionary of `group-name: css-selector` pairs.
Each group name can be referenced by the [group toggle button](use:group-toggle-all).

For example, the following configuration creates two toggle groups

```python
togglebutton_groups = {
  "group1": ".group-one",
  "group2": ".group-two"
}
```

Any elements that match the selector `.group-one` will be assigned to `group1`, and any elements that match the selector `.group-two` will be assigned to `group2`.

:::{warning}
Using `togglebutton_groups` will **override** the value of `togglebutton_selector`.
If you want to manually keep the default selector for toggle-buttons, add a group with the `.toggle, .admonition.dropdown` selector to it.
:::

(use:group-toggle-all)=
### Toggle groups at once with the `{toggle-group}` directive

To toggle all items that belong to the same group at once, use the `{toggle-group}` directive.
It will add a button that, when clicked, will toggle all of the content in a group.
Each item that is closed will be opened, and each item that is open will be closed.

:::{example} Toggle only buttons from one group

Below we define a `{toggle-group}` button that only toggles elements from toggled items that are part of `group1`.

First, define `group1` and `group2` in `conf.py`:

```python
togglebutton_groups = {
  "group1": ".group-one",
  "group2": ".group-two"
}
```

Next, create two blocks of toggled content, one for each group:

````
```{container} group-one
This first content is for **Group One**.
```
```{container} group-one
This second content is for **Group One**.
```
```{container} group-two
This first content is for **Group Two**.
```
```{container} group-two
This second content is for **Group Two**.
```
````
```{container} group-one
This first content is for **Group One**.
```
```{container} group-one
This second content is for **Group One**.
```
```{container} group-two
This first content is for **Group Two**.
```
```{container} group-two
This second content is for **Group Two**.
```

Finally, add a button to toggle **only** group one:

````
```{toggle-group} group1
```
````

results in:

```{toggle-group} group1
```
:::

#### Toggle all groups at once

To toggle all groups with the button, simply do not provide a group name and it will selector all groups.

:::{example} Toggle all buttons regardless of group

The following code will toggle *all* buttons on the page:

````
```{toggle-group}
```
````

```{toggle-group}
```
:::

#### Customize the title of `{toggle-group}`

You may optionally provide a title as well.

:::{example} Custom title with `{toggle-group}`

````
```{toggle-group} tips
:text: Toggle all of the buttons on the page!
```
````

results in:

```{toggle-group} tips
:text: Toggle all of the buttons on the page!
```
:::

### Use the JavaScript function to toggle all buttons

There is also a JavaScript function you can call to trigger the same behavior as the `{toggle-group}` directive described above.

This function is called `toggleAllByGroup` and takes a single argument, which is a group name that you wish to toggle.

You can call it like:

```javascript
toggleAllByGroup("groupname");
```

It is meant for designing your own buttons and UI elements that trigger toggle buttons on the page.

:::{example} Create your own `toggle-groups` button

Here's a toggle-able admonition matching **group1** from above:

````
```{note}
:class: group-one
Here's a toggle-admonition in `group-one`!
```
````
results in:

```{note}
:class: group-one
Here's a toggle-admonition in `group-one`!
```

And the following code embeds a `{raw}` block with custom HTML to trigger this function:

````
```{raw} html
<button onClick="toggleAllByGroup('group1')">Custom button!</button>
```
````

results in:

```{raw} html
<button onClick="toggleAllByGroup('group1')">Custom button!</button>
```
:::

To **toggle all buttons at once** with JavaScript, regardless of group, pass `" "` to the function (i.e., `toggleAllByGroup("**")`).

:::{example} Toggle all buttons with JavaScript
Below are two toggle-buttons from two different groups:

````
```{container} group-one
Group one text!
```
```{container} group-two
Group two text!
```
````

results in:

```{container} group-one
Group one text!
```
```{container} group-two
Group two text!
```

And the following JavaScript button opens both at once:

````
```{raw} html
<button onClick="toggleAllByGroup('**')">Open both!</button>
```
````
results in 

```{raw} html
<button onClick="toggleAllByGroup('**')">Open both!</button>
```
:::

## Customize the toggle button style

There are a few ways you can customize the toggle button style.

### Change toggle button hint text

You can control the "hint" text that is displayed next to togglebuttons.
To do so, use the following configuration variable in your `conf.py` file:

```python
togglebutton_hint = "Displayed when the toggle is closed."
togglebutton_hint_hide = "Displayed when the toggle is open."
```

### Change the toggle icon color

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

## Print behavior with toggle buttons

By default `sphinx-togglebutton` will **open all toggle-able content when you print**.
It will close them again when the printing operation is complete.
To disable this behavior, use the following configuration in `conf.py`:

```python
togglebutton_open_on_print = False
```

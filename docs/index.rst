===================
sphinx-togglebutton
===================

A small sphinx extension to make it possible to add a "toggle button" to
sections of your page.

For example, click the "+" button to the right:

.. note:: Here's a toggled admonition
    :class: toggle

It was created with this code:

.. code:: rst

    .. note:: Here's a toggled admonition
        :class: toggle

        (admonition body here)

And here's a code block:

.. container:: toggle

    .. code:: python

        a = "wow, very python"
        print("this code should be toggle-able!")


Installation
============

You can install `sphinx-togglebutton` with `pip`:

.. code:: bash

    pip install sphinx-togglebutton


Usage
=====

In your ``conf.py`` configuration file, add ``sphinx_togglebutton``
to your extensions list.

E.g.:

.. code:: python

    extensions = [
        ...
        'sphinx_togglebutton'
        ...
    ]

Now, whenever you wish for an admonition to be toggle-able, add the
``:class: toggle`` parameter to the admonition directive that you use.

For example, this code would create a toggle-able "note" admonition:

.. code:: rst

    .. note::
        :class: toggle

        This is my note.

Here's how it looks:

.. note::
    :class: toggle

    This is my note.

Clicking on the toggle button will toggle the item's visibility.


Show content by default
-----------------------

By default, all items with toggle buttons added to them will be hidden by
default. You may also **show the content by default**. To do so, add the
``toggle`` class *as well as* a ``toggle-shown`` class, like so:

.. code:: rst

    .. note::
        :class: toggle, toggle-shown

        This is my note.

This will generate the following block:

.. note::
    :class: toggle, toggle-shown

    This is my note.

Toggle any container of content
-------------------------------

You can also use **containers** to add arbitrary toggle-able code. For example,
here's a container with an image inside:

.. container:: toggle

    .. admonition:: Look at that, an image!

        .. image:: https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif

It was generated with this code:

.. code:: rst

    .. container:: toggle

        .. admonition:: Look at that, an image!

            .. image:: https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif

Here's how they look right after one another:

.. note::
    :class: toggle

    This is my note.

.. note::
    :class: toggle

    This is my second.

Customize the selector words used to toggle content
---------------------------------------------------

``sphinx-togglebutton`` adds a toggle button to elements that are selected
by a CSS selection query. By default, this is ``.toggle``. You can customize
the query that is used with the following Sphinx parameter (in ``conf.py``):

.. code-block:: python

    togglebutton_selector = "<your-selector>

For example, the documentation with this site uses the following configuration
value:

.. code-block:: python

    togglebutton_selector = ".toggle, .secondtoggle"

This means that any element with either of these classes will have toggle
buttons added to them.

.. note::
    :class: secondtoggle

    A note with a ``.secondtoggle`` class.

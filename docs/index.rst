===================
sphinx-togglebutton
===================

A small sphinx extension to make it possible to add a "toggle button" to
sections of your page.

For example, click the "+" button to the right:

.. toggle::

    .. note:: Here's a toggled admonition

It was created with this code:

.. code-block:: rst

    .. toggle::

        .. note:: Here's a toggled admonition

You can also add a title to your toggled block. The title will show up,
and the toggle button will change the block's content. For example:

.. toggle:: Toggle to see what's inside

    It's a code block!

    .. code-block:: python

        a = "wow, very python"
        print("this code should be toggle-able!")


Installation
============

You can install `sphinx-togglebutton` with `pip`:

.. code-block:: bash

    pip install sphinx-togglebutton


Usage
=====

In your ``conf.py`` configuration file, add ``sphinx_togglebutton``
to your extensions list.

E.g.:

.. code-block:: python

    extensions = [
        ...
        'sphinx_togglebutton'
        ...
    ]


The toggle directive
--------------------

To add toggle-able content, use the **toggle directive**. This directive
will wrap its content in a toggle-able container. You can call it like so:

.. code-block:: rst

    .. toggle::

        Here is my toggle-able content!

The code above results in:

.. toggle::

    Here is my toggle-able content!

You can also add titles to your toggle-able content:

.. code-block:: rst

    .. toggle:: My title

        Here is my toggle-able content!

Which results in:


.. toggle:: My title

    Here is my toggle-able content!

To show the toggle-able content by default, use the ``:show:`` flag.

.. code-block:: rst

    .. toggle::
        :show:

        Here is my toggle-able content!

It results in the following:

.. toggle::
    :show:

    Here is my toggle-able content!


Toggling content by adding classes
----------------------------------

You can also make elements toggle-able by adding the ``toggle`` class to
them. This can be done with admonitions and containers with the
``:class: my, classes`` keyword.

For example, this code would create a toggle-able "note" admonition:

.. code-block:: rst

    .. note::
        :class: toggle

        This is my note.

Here's how it looks:

.. note::
    :class: toggle

    This is my note.

Clicking on the toggle button will toggle the item's visibility.


To show the content by default, add a ``toggle-shown`` class as well.

.. code-block:: rst

    .. note::
        :class: toggle, toggle-shown

        This is my note.

This will generate the following block:

.. note::
    :class: toggle, toggle-shown

    This is my note.

Here's how they look right after one another:

.. note::
    :class: toggle

    This is my note.

.. note::
    :class: toggle

    This is my second.

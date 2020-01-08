===================
sphinx-togglebutton
===================

A small sphinx extension to make it possible to add a "toggle button" to
sections of your page.


Installation
============

You can install ``sphinx-togglebutton`` with ``pip``:

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

Clicking on the toggle button will toggle the item's visibility.

You may also **hide the content by default**. To do so, add the ``toggle``
class *as well as* a ``toggle-hidden`` class, like so:

.. code:: rst

    .. note::
        :class: toggle, toggle-hidden

        This is my note.

You can also use **containers** to add arbitrary toggle-able code. For example,
here's a container with an image inside:

.. code:: rst

    .. container:: toggle, toggle-hidden

        .. admonition:: Look at that, an image!

            .. image:: https://media.giphy.com/media/mW05nwEyXLP0Y/giphy.gif

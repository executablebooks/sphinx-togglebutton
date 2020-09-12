===================
sphinx-togglebutton
===================

A small sphinx extension to make it possible to add a "toggle button" to
sections of your page. This allows you to:

- Collapse admonitions (notes, warnings, etc) so that their content is hidden
  until users click a toggle button. See :ref:`dropdown-admonitions`.
- Collapse arbitrary chunks of content on your page with a ``toggle`` directive.
  See :ref:`toggle-directive`.


.. admonition:: For example, click the "+" button to the right:
   :class: dropdown

   Here's a toggled note! You can put all kinds of stuff in here!

You can also add a toggle button to arbitrary chunks of content.
For example, click the toggle button to the right just below.

.. toggle::

    .. admonition:: Wow!
       :class: tip

       It's a code block!

       .. code-block:: python

           a = "wow, very python"

See :ref:`usage` for more information.


.. admonition:: Check out sphinx-panels as well!
   :class: tip

   For a bootstrap-based "dropdown" directive that uses pure CSS, check out
   `Sphinx Panels <https://sphinx-panels.readthedocs.io/en/latest/#dropdown-usage>`_


Installation
============

You can install `sphinx-togglebutton` with `pip`:

.. code-block:: bash

    pip install sphinx-togglebutton

Then, activate it in your ``sphinx`` build by adding it to your ``conf.py`` configuration
file, like so:

E.g.:

.. code-block:: python

    extensions = [
        ...
        'sphinx_togglebutton'
        ...
    ]

See :ref:`usage` for information about how to use ``sphinx-togglebutton``.

.. _usage:

Usage
=====

There are two main ways to use ``sphinx-togglebutton``:

- Collapse admonitions with the ``dropdown`` class
- Make arbitrary chunks of content "toggle-able" with the ``toggle::`` directive

.. caution::

   ``sphinx-togglebutton`` is designed for the
   `sphinx-book-theme <https://sphinx-book-theme.readthedocs.io/>`_. It should work
   properly on other themes, but if you notice any CSS bugs, please open an issue!
   
.. _dropdown-admonitions:

Dropdown admonitions by adding classes
--------------------------------------

Making dropdown admonitions allows you to insert extra information in your document
without forcing the user to see that content. For example:

.. admonition:: What could be inside this warning?
   :class: warning, dropdown

   A whale of a joke!

   .. image:: https://media.giphy.com/media/FaKV1cVKlVRxC/giphy.gif

   (sorry)

Create a dropdown admonition by adding the ``dropdown`` class to an admonition directive.
For example, like so:

.. code-block:: rst

   .. note::
      :class: dropdown

      My note

Note that you can use a custom admonition title and apply the style of a "built-in"
admonition (e.g., ``note``, ``warning``, etc) with the ``admonition::`` directive:

.. code-block:: rst

   .. admonition:: Here's my title
      :class: dropdown, warning

      My note

Creates:

.. admonition:: Here's my title
    :class: dropdown, warning

    My custom admonition!

To show the content by default, add a ``toggle-shown`` class as well.

.. code-block:: rst

    .. note::
        :class: dropdown, toggle-shown

        This is my note.

This will generate the following block:

.. note::
    :class: dropdown, toggle-shown

    This is my note.

.. _toggle-directive:

Toggle any content with the toggle directive
--------------------------------------------

To add toggle-able content, use the **toggle directive**. This directive
will wrap its content in a toggle-able container. You can call it like so:

.. code-block:: rst

    .. toggle::

        Here is my toggle-able content!

The code above results in:

.. toggle::

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


Configuration
=============

Below are a few configuration points for ``sphinx-togglebutton``.


Control the togglebutton hover text
-----------------------------------

You can control the "hint" text that is displayed next to togglebuttons when
their content is collapsed. To do so, use the following configuration variable
in your ``conf.py`` file:

.. code-block:: python

    togglebutton_hint = "My text"

Reference
=========

This is a simple reference section to double-check styling etc.

Here's how they look right after one another:

.. note::
    :class: toggle

    This is my note.

.. note::
    :class: toggle

    This is my second.

.. toggle::

    This is my first.

.. toggle::

    This is my second.

.. admonition:: A really long admonition that will take up multiple lines A really long admonition that will take up multiple lines
    :class: toggle
    
    Admonition content.

    .. image:: https://jupyterbook.org/_static/logo.png

.. admonition:: A really long admonition that will take up multiple lines A really long admonition that will take up multiple lines
    
    Admonition content.

    .. image:: https://jupyterbook.org/_static/logo.png
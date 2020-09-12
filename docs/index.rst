The mako2cli Python Project
==============================

.. toctree::
   :hidden:
   :maxdepth: 1

   license
   reference

This project aim to port the
`Mako Template library <https://www.makotemplates.org/>`_
to a simple command line usage.
The command line could render a template file
using a data source from a yaml file.

Installation
------------

To install the mako2cli Python project,
run this command in your terminal:

.. code-block:: console

   $ pip install mako2cli

Example
-------

Create a file `template.mako` containing:

.. code-block:: mako

    hello ${name}!

And a data file `data.yaml`:

.. code-block:: yaml

    name: world

Now you can render the file with:

.. code-block:: console

    $ m2cli -t template.mako -d data.yaml -o rendered

The output is saved to `rendered`:

.. code-block:: text

    hello world!

That's all!

Usage
-----

Mako2cli usage looks like:

.. code-block:: console

   $ m2cli [OPTIONS]

.. option:: -t, --template PATH  template file (mako)  [required]

   Path to the file containing the template to render.

.. option:: -d, --data PATH  file containing data (YAML)  [required]

   Path to the file containing the data to use for rendering.

.. option:: -o, --output PATH  output file path  [required]

   File that will contain the rendered file.

.. option:: --version

   Display the version and exit.

.. option:: --help

   Display a short usage message and exit.

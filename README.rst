==
py
==

A modern dependency manager for Python.


how to
======

start a new project
-------------------

If you have ``py`` installed globally:

.. code:: sh

    # create your new project dir
    mkdir project
    cd project

    # create a virtual env and a py.toml file in the current dir
    py init


If you do not want to have it installed globally:

.. code:: sh

    # create your new project dir
    mkdir project
    cd project

    # create a virtual env and install py in it
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip install pydepman

    # detects the virtual env and sets it in py.toml
    py init


install a package
-----------------

.. code:: sh

    # add the package and its desired version under [dependencies]
    # e.g. add: django = "3.0.8"
    vim py.toml

    # installs django, asgiref, pytz, sqlparse
    py sync


upgrade a package
-----------------

.. code:: sh

    # edit the respective line under [dependencies]
    # e.g. django = "3.0.8" → django = "3.1"
    vim py.toml

    # upgrades django, asgiref, pytz, sqlparse
    py sync


uninstall a package
-------------------

.. code:: sh

    # remove the respective line from [dependencies]
    # e.g. remove: django = "3.1"
    vim py.toml

    # uninstalls django
    # uninstalls each of asgiref, pytz, sqlparse unless used by another
    # package listed in py.toml (or is listed there itself)
    py sync


commands
========

- ``py init``
    Init a new project (a virtual environment and a py.toml file) in the current directory.

- ``py [SCRIPT]``
    Run python in the virtual environment specified in py.toml. This command makes explicitly activating the virtual environment obsolete.

- ``py search PACKAGE``
    Search for packages in the Cheese Shop.

- ``py show PACKAGE``
    Show the details of a package. It does not matter whether the package is installed locally.

- ``py deps PACKAGE``
    Show the dependency tree of a package. It does not matter whether the package is installed locally.

- ``py sync``
    Install the dependencies (and their dependencies, all the way down) specified in py.toml and uninstall those that are missing. Write requirements.txt.


licence
=======

GPL. You can do what you want with this code as long as you let others do the same.

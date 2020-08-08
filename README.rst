==
py
==

A modern dependency manager for Python.


usage
=====

- ``py [SCRIPT]``
    Run python in the virtual environment specified in py.toml. If there is no py.toml file or it does specify a virtual environment, run with the shell's python executable.
    This command makes explicitly activating the virtual environment obsolete.

- ``py search PACKAGE``
    Search for packages in the Cheese Shop.

- ``py show PACKAGE``
    Show the details of a package. It does not matter whether the package is installed locally.

- ``py deps PACKAGE``
    Show the dependency tree of a package. It does not matter whether the package is installed locally.

- ``py sync``
    Install and uninstall packages as needed to match those specified in the py.toml file.

- ``py install PACKAGE``
    Install a package, optionally with a version specified (e.g. django==3.0.8). The package is installed in the virtual environment specified in the py.toml file.

- ``py upgrade PACKAGE``
    Upgrade a package, preferably with a version specified. By default the package dependencies are also upgraded as necessary.

- ``py uninstall PACKAGE``
    Remove a package from the virtual environment specified in the py.toml file.


licence
=======

GPL. You can do what you want with this code as long as you let others do the same.

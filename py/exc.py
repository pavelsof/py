class PyError(Exception):
    """
    Py's custom exceptions should inherit from this class.
    """
    pass


class ConfigNotFound(PyError):
    """
    Custom exception to be raised when there is not a py.toml in neither the
    current working dir nor in any of its ancestor dirs.
    """
    pass


class ConfigNotReadable(PyError):
    """
    Custom exception to be raised when a py.toml file cannot be read or parsed.
    """
    pass

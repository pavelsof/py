class ConfigNotFound(Exception):
    """
    Custom exception to be raised when there is not a py.toml in neither the
    current working dir nor in any of its ancestor dirs.
    """
    pass


class ConfigNotReadable(Exception):
    """
    Custom exception to be raised when a py.toml file cannot be read or parsed.
    """
    pass

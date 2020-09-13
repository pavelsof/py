import json
from urllib.error import URLError
from urllib.request import Request, urlopen

from pydepman.exc import CheeseShopError


def fetch_package_info(package, version=None):
    """
    Fetch metadata info about a PyPI package, either at a specific version or
    at its latest version (the default).

    Use the PyPI JSON API [1]. Return the retrieved metadata info dict. Raise
    CheeseShopError if something goes wrong.

    [1]: https://warehouse.pypa.io/api-reference/json/
    """
    if version:
        path = '/pypi/{}/{}/json'.format(package, version)
    else:
        path = '/pypi/{}/json'.format(package)

    request = Request(
        'https://pypi.org' + path,
        headers={
            'Accept': 'application/json'
        }
    )

    try:
        with urlopen(request, timeout=5) as response:
            info = json.load(response)

    except URLError as error:
        if hasattr(error, 'code') and error.code == 404:
            message = 'Package not found.'
        else:
            message = 'The PyPI API seems to be down. Please try again later.'
        raise CheeseShopError(message) from error

    except json.JSONDecodeError as error:
        message = (
            'The PyPI API seems to have been changed. '
            'Please open an issue at https://github.com/pavelsof/py/issues'
        )
        raise CheeseShopError(message) from error

    return info

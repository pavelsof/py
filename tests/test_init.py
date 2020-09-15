import os

import toml
from click.testing import CliRunner

from pydepman import cli


def test_fresh(temp_cwd):
    """
    py init should create a virtual env and a py.toml file in the current
    directory if these do not exist already.
    """
    cli_runner = CliRunner(env={'VIRTUAL_ENV': None})

    res = cli_runner.invoke(cli.init)
    assert res.exit_code == 0

    assert os.path.isdir('venv')
    assert os.path.isfile('py.toml')

    with open('py.toml') as f:
        contents = toml.load(f)
        assert contents['venv'] == 'venv'


def test_py_toml_already_exists(temp_cwd):
    """
    py init should abort with an error if there is already a py.toml in the
    current directory.
    """
    with open('py.toml', 'w') as f:
        f.write('hi')

    res = CliRunner().invoke(cli.init)
    assert res.exit_code == 2

import os
import subprocess

import toml

from pydepman.exc import ConfigNotFound, ConfigNotReadable


class Environment:

    def __init__(self):
        """
        Set the default values of the environment attributes and try to find
        and load the relevant py.toml config file.
        """
        self.venv_path = None
        self.deps = []
        self.dev_deps = []
        self.load_config()

    @classmethod
    def find_config(cls, path):
        """
        If there is a py.toml file in the given dir, return its path; if not,
        try finding one in the parent dir.
        """
        config = os.path.join(path, 'py.toml')
        if os.path.isfile(config):
            return config

        parent = os.path.dirname(path)
        if parent == path:
            raise ConfigNotFound

        return cls.find_config(parent)

    def load_config(self):
        """
        Load the nearest py.toml file to be found up the filesystem tree.
        """
        path = self.find_config(os.path.normpath(os.getcwd()))

        try:
            with open(path) as f:
                config = toml.load(f)
        except (OSError, TypeError, toml.TomlDecodeError):
            raise ConfigNotReadable

        if 'venv' in config:
            self.venv_path = config['venv']

        if 'dependencies' in config:
            self.deps = config['dependencies']

        if 'dev-dependencies' in config:
            self.dev_deps = config['dev-dependencies']

    def run(self, cmd):
        """
        Invoke the given command within the environment.
        """
        env = dict(os.environ)

        if self.venv_path:
            env['PATH'] = '{}/bin:{}'.format(self.venv_path, env['PATH'])

        subprocess.run(cmd, env=env)


env = Environment()

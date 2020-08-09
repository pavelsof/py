import click
from click_default_group import DefaultGroup

from py import __version__


@click.group(
    cls=DefaultGroup,
    default='run',
    default_if_no_args=True,
    context_settings={'help_option_names': ['-h', '--help']},
)
@click.version_option(__version__, '-V', '--version')
def main():
    """
    A modern dependency manager for Python.
    """
    pass


@main.command(short_help='Run python. This is the default command.')
@click.argument('script', required=False, type=click.Path(exists=True))
def run(script):
    """
    Run python in the virtual environment specified in py.toml.

    If there is no py.toml file or it does specify a virtual environment, run
    with the shell's python executable.

    This command makes explicitly activating the virtual environment obsolete.
    """
    from py.env import env

    cmd = ['python']
    if script:
        cmd.append(script)

    env.run(cmd)


@main.command(short_help='Search for a package.')
@click.argument('package')
def search(package):
    """
    Search for packages in the Cheese Shop.
    """
    click.echo('searching')


@main.command(short_help='Show the details of a package.')
@click.argument('package')
def show(package):
    """
    Show the details of a package. It does not matter whether the package is
    installed locally.
    """
    pass


@main.command(short_help='Show the dependency tree of a package.')
@click.argument('package')
def deps(package):
    """
    Show the dependency tree of a package. It does not matter whether the
    package is installed locally.
    """
    pass


@main.command(short_help='Sync the installed packages as per py.toml.')
def sync():
    """
    Install the dependencies (and their dependencies, all the way down)
    specified in py.toml and uninstall those that are missing.

    Write requirements.txt.
    """
    from py.env import env

    for package, version in env.deps:
        env.cmd(['pip', 'install', '{}=={}'.format(package, version)])

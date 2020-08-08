import click
from click_default_group import DefaultGroup


@click.group(
    cls=DefaultGroup,
    default='run',
    default_if_no_args=True,
    context_settings={'help_option_names': ['-h', '--help']},
)
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
    click.echo('running')


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


@main.command(short_help='Sync with requirements.txt.')
def sync():
    """
    Install and uninstall packages as needed to match those specified in the
    requirements.txt file.
    """
    pass


@main.command(short_help='Install a package.')
@click.argument('package')
def install(package):
    """
    Install a package, optionally with a version specified. The package is
    installed in the virtual environment specified in the py.toml file.
    """
    pass


@main.command(short_help='Upgrade a package.')
@click.argument('package')
def upgrade(package):
    """
    Upgrade a package, preferably with a version specified. By default the
    package dependencies are also upgraded as necessary.
    """
    pass


@main.command(short_help='Uninstall a package.')
@click.argument('package')
def uninstall(package):
    """
    Remove a package from the virtual environment specified in py.toml.
    """
    pass

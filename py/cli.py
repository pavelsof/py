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

    This command makes explicitly activating the virtual environment obsolete.
    """
    from py.env import env

    cmd = ['python']
    if script:
        cmd.append(script)

    env.run(cmd)


@main.command(short_help='Init a new project.')
@click.option(
    '-p', '--env-path', type=click.Path(exists=False), default='venv',
    help='The directory to create the virtual environment in.'
)
def init(env_path):
    """
    Init a new project in the current directory. This involves two steps:

    (1) Create a virtual environment in $PWD/venv (by default). Skip this step
    if the command is called within an already existing virtual environment.

    (2) Create a py.toml file in which venv points to the virtual environment
    from step 1.

    If the current directory already contains py.toml, abort with an error.
    """
    import os
    import subprocess

    config_file = os.path.join(os.path.normpath(os.getcwd()), 'py.toml')

    if os.path.exists(config_file):
        raise click.UsageError('There is already a py.toml in this directory.')

    if 'VIRTUAL_ENV' in os.environ:
        env_path = os.environ['VIRTUAL_ENV']
    else:
        subprocess.run(['python3', '-m', 'venv', env_path], env=os.environ)
        click.echo('Created a virtual environment in {}'.format(env_path))

    template_file = os.path.join(os.path.dirname(__file__), 'tpl/py.toml')
    with open(template_file) as f:
        config = f.read()

    config = config.format(venv=env_path)

    with open(config_file, 'w') as f:
        f.write(config)

    click.echo('Created py.toml')


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
    from py.http import fetch_package_info
    try:
        info = fetch_package_info(package)
    except Exception as error:
        click.echo(error)
    else:
        fields = [
            ('Name', info['info']['name']),
            ('Version', info['info']['version']),
            ('Summary', info['info']['summary']),
            ('Home-page', info['info']['home_page']),
            ('Author', info['info']['author']),
            ('Author-email', info['info']['author_email']),
            ('License', info['info']['license']),
        ]
        for key, value in fields:
            click.echo('{}: {}'.format(key, value))


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

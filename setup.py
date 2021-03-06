import os.path

from setuptools import setup, find_packages

from pydepman import __version__


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(BASE_DIR, 'README.rst')) as f:
    README = f.read()


setup(
    name='pydepman',
    version=__version__,

    description='A modern dependency manager for Python',
    long_description=README,
    long_description_content_type='text/x-rst',

    url='https://github.com/pavelsof/py',
    author='Pavel Sofroniev',
    author_email='mail@pavelsof.com',

    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
    ],
    keywords='dependency manager',
    project_urls={
        'Source': 'https://github.com/pavelsof/py',
        'Tracker': 'https://github.com/pavelsof/py/issues',
    },

    install_requires=[
        'click ~= 7.1',
        'click-default-group ~= 1.2',
        'pip >= 20.2',
        'toml ~= 0.10',
    ],
    python_requires='>=3',

    packages=find_packages(),
    package_data={
        'pydepman': [
            'tpl/py.toml',
        ]
    },

    entry_points = {
        'console_scripts': [
            'py = pydepman.cli:main'
        ]
    },
)

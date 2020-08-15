"""Command-line interface."""
import click

from . import __version__
from .Renderer import Renderer


@click.command()
@click.option(
    "-t",
    "--template",
    "template",
    type=click.Path(exists=True),
    help="template file (mako)",
    required=True,
)
@click.option(
    "-d",
    "--data",
    "data",
    type=click.Path(exists=True),
    help="file containing data (YAML)",
    required=True,
)
@click.option(
    "-o",
    "--output",
    "output",
    type=click.Path(exists=False),
    help="output file",
    required=True,
)
@click.version_option(version=__version__)
def main(template: str, data: str, output: str) -> None:
    """The mako2cli project."""
    r = Renderer.from_string(template, data, output)
    r.execute()

import click

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
def main(template: str, data: str, output: str) -> None:
    r = Renderer.from_string(template, data, output)
    r.execute()

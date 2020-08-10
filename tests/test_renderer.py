from pathlib import Path

from mako2cli import Renderer


def test_init() -> None:
    Renderer.from_string("template", "data.yaml", "output")


def test_execute(template_file: Path, data_file: Path, template_rendered: str) -> None:
    output_file = Path("/output")
    r = Renderer(template_file, data_file, output_file)
    r.execute()
    assert output_file.open().read() == template_rendered

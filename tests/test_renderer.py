from mako2cli import Renderer
from pathlib import Path

def test_init():
    r = Renderer.from_string('template', 'data.yaml', 'output')

def test_execute(template_file, data_file, template_rendered):
    output_file = Path('/output')
    r = Renderer(template_file, data_file, output_file)
    r.execute()
    assert output_file.open().read() == template_rendered

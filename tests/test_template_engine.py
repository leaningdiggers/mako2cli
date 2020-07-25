import pytest
from pathlib import Path
from mako2cli import TemplateEngine
from mako2cli import TemplateEngineException

def test_init(template_file):
    TemplateEngine.initialize(template_filename=str(template_file)) 
    with pytest.raises(TemplateEngineException):
        TemplateEngine.initialize(template_filename='/unexistent.mako')

def test_render(template_file, data_dict, template_rendered):
    output_file = Path('/output')
    t = TemplateEngine.initialize(template_filename=str(template_file)) 
    t.render(str(output_file), data_dict)
    assert template_rendered == output_file.open().read()


def test_render_error(template_file):
    t = TemplateEngine.initialize(template_filename=str(template_file)) 
    with pytest.raises(TemplateEngineException):
        t.render('/output', {'missing': 'variables'})

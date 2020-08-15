"""Test cases for TemplateEngine module."""
from pathlib import Path
from typing import Dict

from pyfakefs import fake_filesystem
import pytest

from mako2cli import TemplateEngine
from mako2cli import TemplateEngineException


@pytest.fixture
def template_file_syntax_error(fs: fake_filesystem.FakeFilesystem) -> Path:
    """Fixture for create a template file."""
    template_uri = "/template_with_syntax_error.mako"
    fs.create_file(template_uri, contents="hello ${wor")
    return Path(template_uri)


def test_init(template_file: Path) -> None:
    """It correctly initialize."""
    TemplateEngine.initialize(template_filename=str(template_file))


def test_unexistent_template() -> None:
    """It detect missing template file."""
    with pytest.raises(TemplateEngineException):
        TemplateEngine.initialize(template_filename="/unexistent.mako")


def test_template_syntax_error(template_file_syntax_error: Path) -> None:
    """It detect syntax error."""
    with pytest.raises(TemplateEngineException):
        TemplateEngine.initialize(template_filename=str(template_file_syntax_error))


def test_render(template_file: Path, data_dict: Dict, template_rendered: str) -> None:
    """It could render a template using data."""
    output_file = Path("/output")
    t = TemplateEngine.initialize(template_filename=str(template_file))
    t.render(str(output_file), data_dict)
    assert template_rendered == output_file.open().read()


def test_render_error(template_file: Path) -> None:
    """It correctly raise exception if data desn't macth template."""
    t = TemplateEngine.initialize(template_filename=str(template_file))
    with pytest.raises(TemplateEngineException):
        t.render("/output", {"namaae": "variables"})

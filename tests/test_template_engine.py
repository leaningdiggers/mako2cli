"""Test cases for TemplateEngine module."""
from pathlib import Path
from typing import Dict

import pytest

from mako2cli import TemplateEngine
from mako2cli import TemplateEngineException


def test_init(template_file: Path) -> None:
    """It correctly initialize."""
    TemplateEngine.initialize(template_filename=str(template_file))
    with pytest.raises(TemplateEngineException):
        TemplateEngine.initialize(template_filename="/unexistent.mako")


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

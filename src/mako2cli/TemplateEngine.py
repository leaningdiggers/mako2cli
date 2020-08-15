"""Template Engine module."""
from __future__ import annotations

from pathlib import Path
from typing import Dict, Type

import attr
from mako import exceptions
from mako.template import Template


class TemplateEngineException(Exception):
    """Generic module exception."""

    pass


@attr.s
class TemplateEngine:
    """Manage the template logic rendering.

    Attributes:
        template: Mako template object
    """

    template = attr.ib(type=Template)

    @classmethod
    def initialize(cls: Type[TemplateEngine], template_filename: str) -> TemplateEngine:
        """Factory method for class creation.

        Args:
            template_filename (str): file with template logic to render.

        Returns:
            TemplateEngine intialized object

        Raises:
            TemplateEngineException: if file contains invalid syntax.
        """
        try:
            template = Template(filename=template_filename)
            return cls(template)
        except exceptions.MakoException:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException("Error initializing TemplateEngine.")
        except OSError:
            raise TemplateEngineException(f"File not found {template_filename}.")

    def render(self: TemplateEngine, output_file_name: str, data: Dict) -> None:
        """Render the template.

        Execute the template rendering given a data set.

        Args:
            output_file_name (str): output file rendering.
            data (Dict): data to use for rendering.

        Raises:
            TemplateEngineException: if file contains invalid syntax.
        """
        try:
            output_file = Path(output_file_name)
            output_file.write_text(self.template.render(**data))
        except NameError:
            raise TemplateEngineException("Missing data for template.")

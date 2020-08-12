"""Renderer module."""
from __future__ import annotations

from pathlib import Path
from typing import Type

import attr

from .DataLoader import DataLoader
from .TemplateEngine import TemplateEngine


@attr.s
class Renderer:
    """Execute a template rendering gived data file.

    This class manage the template rendering from a data file.

    Attributes:
        template_file (Path): file with template logic to render.
        data_file (Path): data to use for rendering
        output_file (Path): file containing the rendering output.
    """

    template_file = attr.ib(type=Path)
    data_file = attr.ib(type=Path)
    output_file = attr.ib(type=Path)

    @classmethod
    def from_string(
        cls: Type[Renderer], template_file: str, data_file: str, output_file: str
    ) -> Renderer:
        """Factory method used for string filenames.

        Args:
            template_file (str): file with template logic to render.
            data_file (str): data to use for rendering.
            output_file (str): file containing the rendering output.
        """
        return cls(Path(template_file), Path(data_file), Path(output_file))

    def execute(self: Renderer) -> None:
        """Execute the rendering process, generate the output file."""
        d = DataLoader(self.data_file)
        t = TemplateEngine.initialize(template_filename=str(self.template_file))
        t.render(str(self.output_file), d.get_data())

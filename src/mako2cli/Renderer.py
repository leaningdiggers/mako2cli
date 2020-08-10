from __future__ import annotations

from pathlib import Path
from typing import Type

import attr

from .DataLoader import DataLoader
from .TemplateEngine import TemplateEngine


@attr.s
class Renderer:
    template_file = attr.ib(type=Path)
    data_file = attr.ib(type=Path)
    output_file = attr.ib(type=Path)

    @classmethod
    def from_string(
        cls: Type[Renderer], template_file: str, data_file: str, output_file: str
    ) -> Renderer:
        return cls(Path(template_file), Path(data_file), Path(output_file))

    def execute(self: Renderer) -> None:
        d = DataLoader(self.data_file)
        t = TemplateEngine.initialize(template_filename=str(self.template_file))
        t.render(str(self.output_file), d.get_data())

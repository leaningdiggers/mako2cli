from __future__ import annotations

from pathlib import Path
from typing import Dict, Type

import attr
from mako import exceptions
from mako.lookup import TemplateLookup
from mako.template import Template


class TemplateEngineException(Exception):
    pass


@attr.s
class TemplateEngine:
    template = attr.ib(type=Template)

    @classmethod
    def initialize(cls: Type[TemplateEngine], template_filename: str) -> TemplateEngine:
        try:
            lookup = TemplateLookup(directories=("."))
            template = lookup.get_template(template_filename)
            return cls(template)
        except exceptions.MakoException:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

    def render(self: TemplateEngine, output_file_name: str, data: Dict) -> None:
        try:
            output_file = Path(output_file_name)
            output_file.write_text(self.template.render(**data))
        except (exceptions.MakoException, NameError):
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

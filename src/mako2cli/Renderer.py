import attr
from .DataLoader import DataLoader
from .TemplateEngine import TemplateEngine
from pathlib import Path

@attr.s
class Renderer():
    template_file = attr.ib(type=Path)
    data_file = attr.ib(type=Path)
    output_file = attr.ib(type=Path)
    
    @classmethod
    def from_string(cls,
                    template_file: str,
                    data_file: str,
                    output_file: str):
        return cls(Path(template_file),
                   Path(data_file),
                   Path(output_file))

    def execute(self):
        d = DataLoader(self.data_file)
        t = TemplateEngine.initialize(
                template_filename=str(self.template_file),
                template_directories_list='.')
        t.render(self.output_file, d.get_data())

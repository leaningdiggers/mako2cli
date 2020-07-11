from pathlib import Path
from mako.lookup import TemplateLookup
from mako import exceptions


class TemplateEngineException(Exception):
    pass


class TemplateEngine():
    def __init__(self,
                 template_name=None,
                 template_directories_list=None,
                 data=None):
        try:
            self.lookup = TemplateLookup(directories=template_directories_list)
            self.template = self.lookup.get_template(template_name)
            self.data = data
        except:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

    def render(self):
        try:
            return self.mytemplate.render(**self.data)
        except:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

    def render_on_file(self, filename):
        try:
            file = Path(filename)
            file.write_text(self.template.render(**self.data))
        except:
            print(exceptions.text_error_template().render())
            raise TemplateEngineException()

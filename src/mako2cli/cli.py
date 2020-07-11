import click
from .DataLoader import DataLoader
from .TemplateEngine import TemplateEngine

@click.command()
@click.option('-t', '--template', 'template',
              type=click.Path(exists=True),
              help='template file (mako)',
              required=True)
@click.option('-d', '--data', 'data',
              type=click.Path(exists=True),
              help='file containing data (YAML)',
              required=True)
@click.option('-o', '--output', 'output',
              type=click.Path(exists=False),
              help='output file',
              required=True)
def main(template, data, output):
    d = DataLoader.from_string(data)
    t = TemplateEngine(template_name=template,
                       data=d.get_data(),
                       template_directories_list='.')
    t.render_on_file(output)

if __name__ == '__main__':
    main()

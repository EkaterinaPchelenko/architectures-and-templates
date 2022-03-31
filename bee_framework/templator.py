from jinja2 import Template
import os


def render(temp_name, folder='templates', **kwargs):

    file_path = os.path.join(folder, temp_name)
    with open(file_path, encoding='utf-8') as file:
        template = Template(file.read())
    return template.render(**kwargs)
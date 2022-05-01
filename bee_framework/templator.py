from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
import os


def render(temp_name, folder='templates', **kwargs):

    environment = Environment()
    environment.loader = FileSystemLoader(folder)
    template = environment.get_template(temp_name)
    return template.render(**kwargs)
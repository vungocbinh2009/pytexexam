from jinja2 import Environment, PackageLoader

jinja_env = Environment(
    loader=PackageLoader('pytexexam', 'templates'),
    autoescape=False
)

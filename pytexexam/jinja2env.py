from jinja2 import Environment, PackageLoader

# Jinja environment
jinja_env = Environment(
    loader=PackageLoader('pytexexam', 'templates'),
    autoescape=False
)

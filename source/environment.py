from jinja2 import Environment, PackageLoader

jinja2_environment = Environment(
    loader = PackageLoader("environment", "templates"),
    trim_blocks = True,
    lstrip_blocks = True
)

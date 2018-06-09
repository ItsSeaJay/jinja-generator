from environment import jinja2_environment

templates = {
    "portfolio": jinja2_environment.get_template("portfolio.html"),
    "project": jinja2_environment.get_template("project.html")
}

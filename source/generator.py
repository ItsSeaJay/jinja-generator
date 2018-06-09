import folder
from markdown import markdown
import jinja2
import json
import os
import shutil
import uri
from templates import templates

class Generator:
    build_folder = "_build"

    def __init__(object):
        pass

    """Generates a site to the current build folder"""
    def generate(self):
        # Create the build folder if it doesn't already exist
        if os.path.isdir(self.build_folder):
            folder.clear(self.build_folder)
        else:
            try:
                os.makedirs(self.build_folder)
            except OSError as error:
                print(error)

        # Get JSON data to feed into templates
        data = self.get_json("data/data.json")
        # Add extra data from config file
        config = self.get_json("data/config.json")
        data["base_url"] = config["base_url"]
        data["analytics_id"] = config["analytics_id"]
        data["language"] = config["language"]

        # Copy root data into build folder
        folder.copy_list("boilerplate", self.build_folder)
        # Add style sheets to the build folder
        folder.copy("css", self.build_folder + "/css")
        # Add appropriate scripts on top of those
        folder.copy("js", self.build_folder + "/js")

        # Generate website content
        self.output_index(data)
        self.output_projects(data["projects"])

    """
    Gets the JSON data to pass into templates
    as a Python dictionary
    """
    def get_json(self, path):
        with open(path) as data_file:
            contents = data_file.read()
            data = json.loads(contents)

        return data

    """
    Outputs the website index file
    This should be the front page of the website
    """
    def output_index(self, data):
        path = self.build_folder + "/index.html"

        with open(path, "w") as index:
            render = index.write(templates["portfolio"].render(data))

        return render

    """Outputs an HTML page for each project in the data.json file"""
    def output_projects(self, projects):
        # Make the projects folder
        os.makedirs(self.build_folder + "/projects")

        # Create an index file for each project
        for project in projects:
            indicator = uri.generate(project["title"])

            path = self.build_folder + "/projects/" + indicator
            os.makedirs(path)
            path += "/index.html"

            with open(path, "w") as index:
                index.write(templates["project"].render(project))

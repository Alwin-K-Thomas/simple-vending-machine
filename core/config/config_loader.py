""" Class to handle the config system for the vending machine
"""
import json
import os


class ConfigLoader:
    """ Config class to load the json file which contains the vending machine
        inventory and accepted conditions.
    """
    @staticmethod
    def load_config():
        """ Function to load/create the config from the json file.
        """
        config_path = os.path.join(os.path.dirname(__file__), "config.json")
        with open(config_path, "r") as file:
            return json.load(file)

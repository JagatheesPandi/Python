import json
from utils.pathManager import *

class JsonLoader:
    @staticmethod
    def load():
        config_file = PathManager.CONFIG/'config.json'
        with open(config_file, 'r') as file:

            return json.load(file)

# config = ConfigLoader.load()

# print(config["min_accuracy"])

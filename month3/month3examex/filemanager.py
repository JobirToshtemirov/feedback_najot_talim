import json
import os

class FileManager:

    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                json.dump([], file)

    def read_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def write_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)

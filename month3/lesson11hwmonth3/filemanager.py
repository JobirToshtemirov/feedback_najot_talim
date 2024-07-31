import json
import os

class FileManager:
    def __init__(self, filename ='month3/lesson11hwmonth3/data/scooters.json'):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as file:
                json.dump({'admin_password': 'admin', 'scooters' : {}}, file )

    def load_data(self):
        with open(self.filename, 'r') as file:
            return json.load(file)

    def save_data(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

    def get_data(self, key):
        data = self.load_data()
        return data.get(key, None)

    def update_data(self, key, value):
        data = self.load_data()
        data[key] = value
        self.save_data(data)

    def delete_data(self, key):
        data = self.load_data()
        if key in data:
            del data[key]
            self.save_data(data)

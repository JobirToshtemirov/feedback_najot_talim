
import os
import json
import hashlib

#class file manager for save data and to manage
class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existence(self): #check file 
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0

    def read_json_file(self): #read file
        if self.check_existence():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []

    def write_to_json(self, all_data): #write file
        with open(self.file_name, 'w') as file:
            json.dump(all_data, file, indent=4)

    def add_data(self, data: dict): #add data to file
        all_data = self.read_json_file()
        all_data.append(data)
        self.write_to_json(all_data)
        return "Data is added"
    
    def update_data(self, key, value):
        data = self.load_data()
        data[key] = value
        self.save_data(data)

filemanager = FileManager('renthouse.json')
filemanager1 = FileManager('applications.json')

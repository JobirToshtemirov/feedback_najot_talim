"""
Men kitob do'kon ochmoqchiman, va meni sotuvlarimni boshqarish uchun dastur kerak
Unda quyidagi imkoniyatlar bo'lishi kerak

Users:
    - hamma kitoblarni ro'yxatini ko'rish
    - kitobni nomi bo'yicha qidirish
    - kitobni nechtadir sotib sotib olish
    - sotib olgan kitoblari ro'yxatini ko'rish
    - logout

Admins:
    - kitob qo'shish
    - kitobni o'chirish
    - kitobni quantity sini o'zgartirish
    - kitobni nomi bo'yicha qidirish
    - hamma ro'yxatdan o'tgan userlarni ko'rish
    - logout
"""

"""
Arxitektura:
1.class FileManager for save  data 
2. class Store for user and admin
    2.1 method show all books
    2.2 method search book with name 
    2.3 method sale book 
    2.4show my books
    2.exit menu
     add books
     delete books
     
3. menu
    3.1 fegistration
    3.2 login
    3.2.1 user menu
        - hamma kitoblarni ro'yxatini ko'rish
        - kitobni nomi bo'yicha qidirish
        - kitobni nechtadir sotib sotib olish
        - sotib olgan kitoblari ro'yxatini ko'rish
        - logout
    3.2.2 admin menu
        - kitob qo'shish
        - kitobni o'chirish
        - kitobni quantity sini o'zgartirish
        - kitobni nomi bo'yicha qidirish
        - hamma ro'yxatdan o'tgan userlarni ko'rish
        - logout main menu
    3.3 exit  
"""

import json
import os 
import hashlib



import os
import json
import hashlib

#admin info
ADMIN_LOGIN = "Jobir"
ADMIN_PASSWORD = "Toshtemirov"


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

file_manager = FileManager('teams.json')






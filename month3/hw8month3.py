#htask 8
"""
GM mashinalariga buyurtma berish uchun sistema tuzish kerak:
Login qilgan foydalanuvchidan qanyda mashina olmoqchi ekanligini so'rash
kerak va uni ro'yxatga qo'shib qo'yish kerak:

Logindan keyingi menu:
    1. Ariza topshirish
    2. Mening arizalarim
    3. Logout

Register, Login, Logout uchun mantiq yozing
users.json file da foydalanuvchilarni saqlashingiz mumkin, login qilgan userni aniqlash
uchun is_login yoki shunga o'xshash o'zgaruvchi qo'shib ketsangiz bo'ladi.
Logout bo'lganda esa hamma foydalanuvcilarni is_login o'zgaruvchisini false qilib chiqsangiz bo'ladi

Ikkita class yozishingiz mumkin, birinchisi user objectlarini yasash valogin, register, logoutlarni
boshqarish uchun ikkinchisi json file bilan ishlash uchun
"""

import os
import json
import hashlib


class FileManager: #class file manager
    def __init__(self, file_name):
        self.file_name = file_name

    def check_existance(self): #check existance
        return os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0
      
      #read json file
    def read_json_file(self):
        if self.check_existance():
            with open(self.file_name, 'r') as file:
                return json.load(file)
        return []
    
    #write to json file
    def write_to_json(self, all_data):
        with open(self.file_name, mode='w') as file:
            json.dump(all_data, file, indent=4)
    #add data 
    def add_data(self, data: dict):
        all_data = self.read_json_file()
        all_data.append(data)
        self.write_to_json(all_data)
        return "Data is added"

file_manager = FileManager('users.json')

class User:
    def __init__(self, client_name, client_id, client_password) -> None:
        self.client_name = client_name
        self.client_id = client_id
        self.client_password = client_password
        self.is_login = False

    def check_password(self, confirm_password):
        return self.client_password == confirm_password

    @staticmethod
    def hash_password(client_password):
        return hashlib.sha256(client_password.encode()).hexdigest()

def royhatdan_otish():
    client_name = input("Enter your name: ")
    client_id = input("Enter your id: ")
    client_password = input("Enter your password: ")
    confirm_password = input("Enter your confirm password: ")

    user = User(client_name, client_id, client_password)
    if not user.check_password(confirm_password):
        print("Password is wrong")
        return royhatdan_otish()

    user.client_password = User.hash_password(client_password)
    file_manager.add_data(data=user.__dict__)
    return show_first_menu()

def login():
    client_id = input("Enter your id: ")
    client_password = input("Enter your password: ")

    hashed_password = User.hash_password(client_password)
    all_users = file_manager.read_json_file()

    for user in all_users:
        if user['client_id'] == client_id and user['client_password'] == hashed_password:
            user['is_login'] = True
            file_manager.write_to_json(all_users)
            return show_second_menu()

    print("user is not found or incorrect password")
    print("enter yor choice")
    return show_first_menu()

def logout_all():
    all_users = file_manager.read_json_file()
    for user in all_users:
        user['is_login'] = False
    file_manager.write_to_json(all_users)
    return show_first_menu()

def submit_application():
    application = input("Enter your favourite car ")
    all_users = file_manager.read_json_file()
    for user in all_users:
        if user['is_login']:
            if 'applications' not in user:
                user['applications'] = []
            user['applications'].append(application)
            file_manager.write_to_json(all_users)
            print("Application added succesfully!")
            return show_second_menu()

def view_applications():
    all_users = file_manager.read_json_file()
    for user in all_users:
        if user['is_login']:
            if 'applications' in user:
                print("your aplications:", user['applications'])
            else:
                print("you dont have aplications.")
            return show_second_menu()

def show_second_menu():
    menu = """
1. Ariza topshirish
2. Mening arizalarim
3. Logout
"""
    print(menu)
    user_input = input("enter your choice: ")
    if user_input == "1":
        submit_application()
    elif user_input == "2":
        view_applications()
    elif user_input == "3":
        logout_all()
    else:
        print("incorrect choice enter egain")
        show_second_menu()

def show_first_menu():
    menu = """
    1. Royhatdan otish
    2. Login(orqali kirish)
    3. Chiqish
"""
    print(menu)
    user_input = input("enter your choice: ")
    if user_input == "1":
        royhatdan_otish()
    elif user_input == "2":
        login()
    elif user_input == "3":
        print("good bye!")
        return
    else:
        print("incorect choice try again.")
        show_first_menu()

if __name__ == "__main__":
    logout_all()

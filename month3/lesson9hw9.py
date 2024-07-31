""" Hakatonga jamoalar ro'yxatdan o'tishlari uchun dastur tuzing. 
Har bir jamoada kamida 3 ta odam bo'lishi kerak, jamoani nomi ham bo'lishi kerak. 
Jamoa sardori o'zini jamoasi haqida malumotni kiritadi, 
admin odam esa hamma ro'yxatdan o'tgan jamoalar haqida malumotni ko'ra olishi va o'chira olishi kerak. 
Ma'lumotlarni qanday va qaysi faylda saqlash o'zizga bog'liq, qanday class lar yozish ham. 
Menu li bo'lishi kerak, admin sifatida kirish uchun login ishlatish kerak, oddiy hakatonga ro'yxatdan o'tish uchun esa shart emas 
"""

"""
Arxitektura:
1. class File manager
2. class Hakaton
    2.1 method  komanda shakillantirish
3. menu 
    3.1 jamoa shakillantirish 
    3.2 login
        (admin menu)
        3.2.1 barcha jamoalarni korish 
        3.2.2 komanda ochirish
        3.2.3 bosh menuga qaytish
        3.2.4 exit 
    3.3 exit

"""

# htask

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

#class hakaton and methods 
class Hakaton:
    @staticmethod
    def hash_password(password): #hashlib for hash  admin password 
        return hashlib.sha256(password.encode()).hexdigest()

    def __init__(self, team_name, team_captain, members):
        self.team_name = team_name
        self.team_captain = team_captain
        self.members = members

    def to_dict(self): #method dict how save in file
        return {
            'team_name': self.team_name,
            'team_captain': self.team_captain,
            'members': self.members
        }
 # method for appliction teams
def submit_application():
    team_name = input("komanda nomini kiritng: ")
    team_captain = input("komanda sardorini ismini kiriting: ")
    members = []
 # her if members less 3 not add and  not save  
    while len(members) < 3:
        member = input(f"ishtirokchi ismini kiriting {len(members) + 1}: ")
        members.append(member)

 # here if you want add member you must enter xa or yoq
    while True:
        more_members = input("ishtirokchi qoshishni istaysizmi? (yoq/xa): ").strip().lower()
        if more_members == 'xa':
            member = input(f"ishtirokchi ismini kiritng {len(members) + 1}: ")
            members.append(member)
        elif more_members == 'yoq':
            break
        else:
            print("iltimos, quydagilardan birini tanlang 'xa' / 'yoq'.")

        #creating object
    team = Hakaton(team_name, team_captain, members)
    file_manager.add_data(team.to_dict())
    print("komanda muovfaqiyatli qoshildi!")
    return show_menu()

# login for admin/s
def login():
    admin_login = input("admin loginini kiriting: ")
    admin_password = input("admin parolini kiriting: ")
    if admin_login == ADMIN_LOGIN and Hakaton.hash_password(admin_password) == Hakaton.hash_password(ADMIN_PASSWORD):
        return show_admin_menu()
    else:
        print("notogri login yoki parol kiritildi qayta urinib koring.")
        return show_menu()
    
# method show all teams for admin menu
def show_teams():
    teams = file_manager.read_json_file()
    if teams:
        for id_ornumber, team in enumerate(teams):
            print(f"komanda {id_ornumber + 1}: {team['team_name']}, sardor: {team['team_captain']}, ishtirokchilar: {', '.join(team['members'])}")
    else:
        print("bunday jamoa yoq.")
    return show_admin_menu()

# method delete team for admin menu
def delete_team():
    teams = file_manager.read_json_file()
    if teams:
        for id_ornumber, team in enumerate(teams):
            print(f"{id_ornumber + 1}. komanda: {team['team_name']}, sardor: {team['team_captain']}, ishtirokchilar: {', '.join(team['members'])}")
        
        try:
            team_id_ornumber = int(input("ochirish uchun komanda raqamini kiriting: ")) - 1
            if 0 <= team_id_ornumber < len(teams):
                teams.pop(team_id_ornumber)
                file_manager.write_to_json(teams)
                print("komanda muovfaqiyatli ochirildi.")
            else:
                print("notogri komanda raqami.")
        except ValueError:
            print("iltimos komandani togri raqamini kiriting.")
    else:
        print("komanda topilmadi.")
    return show_admin_menu()

# method show menu for users 
def show_menu():
    menu = """
1. komanda qoshish
2. admin kabineti
3. chiqish
"""
    print(menu)
    try:
        user_input = input("tanlang: ")
        if user_input == "1":
            submit_application()
        elif user_input == "2":
            login()
        elif user_input == "3":
            print("xayr!")
        else:
            print("notogri tanlov ! qayta urinib koring.")
            show_menu()
    except ValueError:
        print("iltimos menudan birortasini tanlang.")
        show_menu()

# method show admin menu for admin
def show_admin_menu():
    menu = """
1. barcha komandalarini korish
2. komanda ochirish
3. bosh menuga qaytish
4. chiqish
"""
    print(menu)
    try:
        user_input = input("tanlang: ")
        if user_input == "1":
            show_teams()
        elif user_input == "2":
            delete_team()
        elif user_input == "3":
            show_menu()
        elif user_input == "4":
            print("xayr!")
        else:
            print("notogri tanlov qayta urinib koring.")
            show_admin_menu()
    except ValueError:
        print("iltimos munu dan birortasini tanlang.")
        show_admin_menu()

if __name__ == "__main__":
    show_menu()

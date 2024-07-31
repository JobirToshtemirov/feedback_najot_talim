from main import show_menu,show_admin_menu
from filemanager import file_manager


#admin info
ADMIN_LOGIN = "Jobir"
ADMIN_PASSWORD = "Toshtemirov"

def login():
    admin_login = input("admin loginini kiriting: ")
    admin_password = input("admin parolini kiriting: ")
    if admin_login == ADMIN_LOGIN and Hakaton.hash_password(admin_password) == Hakaton.hash_password(ADMIN_PASSWORD):
        return show_admin_menu()
    else:
        print("notogri login yoki parol kiritildi qayta urinib koring.")
        return show_menu()
    
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


def show_teams():
    teams = file_manager.read_json_file()
    if teams:
        for id_ornumber, team in enumerate(teams):
            print(f"komanda {id_ornumber + 1}: {team['team_name']}, sardor: {team['team_captain']}, ishtirokchilar: {', '.join(team['members'])}")
    else:
        print("bunday jamoa yoq.")
    return show_admin_menu()





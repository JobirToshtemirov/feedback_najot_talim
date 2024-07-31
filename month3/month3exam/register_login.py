from main import rent_menu , main_menu
from filemanager import FileManager

class Renthouse:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def register(self, username, password):
        if username in self.users:
            print("bu isim boyicha user mavjud.")
            return False
        self.users[username] = username 
        self.filemanager.update_data(self.users)
        print("registratsiya yaxshi yakkulandi.")
        return True

    def login(self,user_login,user_password):
        user_login_input = input("user loginini kiriting: ")
        user_password_input = input("user parolini kiriting: ")
        if user_login_input == user_login and user_password_input == user_password:
            return rent_menu()
        else:
            print("notogri login yoki parol kiritildi qayta urinib koring.")
            return main_menu()
        
    def logout_all(self):
        all_users = FileManager.read_json_file()
        index = 0
        while index < len(all_users):
            all_users[index]['is_login'] = False
            index += 1
        FileManager.write_to_json(all_users)
        return main_menu()



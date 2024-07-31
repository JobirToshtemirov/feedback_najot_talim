import hashlib
from filemanager import FileManager

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

class UserManager:
    def __init__(self, file_path):
        self.file_manager = FileManager(file_path)
        self.users = self.file_manager.get_data()

    def register(self, username, password):
        if username in self.users:
            print("bu isim boyicha user mavjud.")
            return False
        self.users[username] = User.hash_password(password)
        self.file_manager.update_data(self.users)
        print("registratsiya yaxshi yakkulandi.")
        return True

    def login(self, username, password):
        password_hash = User.hash_password(password)
        if username in self.users and self.users[username] == password_hash:
            print("kirish yaxshi yakunlandi.")
            return True
        else:
            print("notogri isim yoki parol kiritildi.")
            return False
        


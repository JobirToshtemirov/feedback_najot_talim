from filemanager import FileManager

class RegisterLogin:
    def __init__(self, user_file):
        self.file_manager = FileManager(user_file)

    def register(self, username, password):
        users = self.file_manager.read_data()
        for user in users:
            if user['username'] == username:
                print("Username already exists.")
                return False
        users.append({'username': username, 'password': password, 'houses': [], 'applications': [], 'comments': []})
        self.file_manager.write_data(users)
        return True

    def login(self, username, password):
        users = self.file_manager.read_data()
        for user in users:
            if user['username'] == username and user['password'] == password:
                return user
        print("Invalid username or password.")
        return None

    def logout(self, user):
        print(f"User {user['username']} logged out.")
        return None

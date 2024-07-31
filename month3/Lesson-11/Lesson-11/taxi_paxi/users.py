import hashlib
from typing import Union

from file_manager import user_manager

admin_id = "00"
admin_password = "00"


class User:
    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password
        self.is_login = False

    def check_password(self, confirm_password):
        return confirm_password == self.password

    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()


def register() -> bool:
    try:
        full_name = input("Enter full name: ")
        username = input("Enter username: ")
        password = input("Enter your password: ")
        confirm_password = input("Enter your confirm password: ")

        student = User(full_name, username, password)
        if not student.check_password(confirm_password):
            print("Passwords do not match")
            return register()

        student.password = User.hash_password(password)
        user_manager.add_data(data=student.__dict__)
        print("You have successfully registered")
        return True
    except Exception as e:
        print(f"Something went wrong {e}")
        return False


def login() -> dict:
    username = input("Enter username: ")
    password = input("Enter your password: ")
    if username == admin_id and password == admin_password:
        return {'is_admin': True, 'success': True}
    hashed_password = User.hash_password(password)

    all_users = user_manager.read()

    index = 0
    while index < len(all_users):
        if all_users[index]['username'] == username and all_users[index]['password'] == hashed_password:
            all_users[index]['is_login'] = True
            user_manager.write(all_users)
            return {'is_admin': False, 'success': True}
        index += 1
    user_manager.write(all_users)
    print("User not found, or password is incorrect")
    return {'is_admin': False, 'success': False}


def logout_all() -> None:
    all_users = user_manager.read()
    index = 0
    while index < len(all_users):
        all_users[index]['is_login'] = False
        index += 1
    user_manager.write(all_users)


def active_user() -> Union[dict, bool]:
    users = user_manager.read()
    for user in users:
        if user['is_login']:
            return user
    return False

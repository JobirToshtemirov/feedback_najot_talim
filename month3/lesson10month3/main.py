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
     
3. menu
    3.1 fegistration
    3.2 login
        3.2.1 user menu
        3.2.2 admin menu
    3.3 exit  
"""


import hashlib
from typing import Union
from admin import login, submit_application, delete_team, show_teams
from users import register, active_user, login,logout_all
from filemanager import user_manager, books_manager, order_manager


def show_admin_menu():
    text = """
        1. Add book: 
        2. Update book quantity: 
        3. Delete book: 
        4. Search book with name:
        5. Show all orders:
        6. Show all users:
        7. Logout: 
    """
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        pass
    elif user_input == "2":
        pass


def show_menu():
    text = """
    1. Buy book: 
    2. My orders: 
    3. Show all books:
    4. Search book with name:
    3. Logout: 
"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        logout_all()
        return show_auth_menu()
    else:
        print("Good bye !")
        return


def show_auth_menu():
    text = """
    1. Register
    2. Login
    3. Exit
"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if register():
            show_auth_menu()
    elif user_input == "2":
        data = login()
        if data['success'] and data['is_admin']:
            return show_admin_menu()
        else:
            return show_menu()

    elif user_input == "3":
        print("Good bye !")
        return
    else:
        print("Wrong choice !")
        return show_auth_menu()


if __name__ == "__main__":
    logout_all()
    show_auth_menu()

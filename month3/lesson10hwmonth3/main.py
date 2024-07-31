""" Kitoblarni alishish uchun dastur tuzish kerak. 
Tasavvur qiling sizda o'qilgan bir kitob bor va siz yangi kitob olmoqchisiz lekin pulingiz yo'q 
va yana kimdadir shunday holat lekin u o'qigan kitob sizga kerak siz o'qigan kitob esa unga kerak. 
Mana shu muommo yechish uchun dastur tuzish kerak. 
Qanday mantiq bilan ishlashi o'zingizga bo'g'liq muhimi mana shu muommo yechsangiz bo'ldi. 
Albatta register, login, logout bo'lishi kerak """

# htask


import os
from users import UserManager
from book_manager import BookManager

DATA_DIR = 'month3/lesson10hwmonth3/data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
BOOKS_FILE = os.path.join(DATA_DIR, 'books.json')

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    user_manager = UserManager(USERS_FILE)
    book_manager = BookManager(BOOKS_FILE)

    while True:
        print("\nasosiy menu:")
        print("1. registration")
        print("2. login")
        print("3. exit")
        choice = input("menudan birini tanlang: ")

        if choice == '1':
            username = input("ismingizni kiriting: ")
            password = input("parolingizni kiriting: ")
            user_manager.register(username, password)
        elif choice == '2':
            username = input("ismingizni kiriting: ")
            password = input("parolingizni kiriting: ")
            if user_manager.login(username, password):
                print(f"xush kelibsiz, {username}")
                logged_in_menu(username, book_manager)
        elif choice == '3':
            break
        else:
            print("notogri tanlov , qayta urinib koring.")

def logged_in_menu(username, book_manager):
    while True:
        print("\nuser menu:")
        print("1. kitob qoshish")
        print("2. kitoblar royhati")
        print("3. kitob almashtirishga sorov yuborish")
        print("4. chiqish")
        choice = input("menudan birini tanlang: ")

        if choice == '1':
            title = input("kitob nomini kiriting: ")
            book_manager.add_book(username, title)
        elif choice == '2':
            book_manager.list_books()
        elif choice == '3':
            book_id = input("kitob  id sini kiriting: ")
            book_manager.request_trade(book_id, username)
        elif choice == '4':
            break
        else:
            print("notogri tanlov, qayta urinib koring.")

if __name__ == "__main__":
    main()
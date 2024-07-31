""" Kitoblarni alishish uchun dastur tuzish kerak. 
Tasavvur qiling sizda o'qilgan bir kitob bor va siz yangi kitob olmoqchisiz lekin pulingiz yo'q 
va yana kimdadir shunday holat lekin u o'qigan kitob sizga kerak siz o'qigan kitob esa unga kerak. 
Mana shu muommo yechish uchun dastur tuzish kerak. 
Qanday mantiq bilan ishlashi o'zingizga bo'g'liq muhimi mana shu muommo yechsangiz bo'ldi. 
Albatta register, login, logout bo'lishi kerak """

# htask


import os
from users import UserManager
from filemanager import 

DATA_DIR = 'month3/lesson11/data'
USERS_FILE = os.path.join(DATA_DIR, 'users.json')
TAXIS_FILE = os.path.join(DATA_DIR, 'taxis.json')

def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    user_manager = (USERS_FILE)
    book_manager = (TAXIS_FILE)

def show_menu():
    text ="""
    1.add announcement as a taxi
    2.add ammouncement as a client
    3.filter taxis
    4.filter cients
    5.show my announcement
    6.logout
"""
    print(text) 
user_input =input("enter your choice ")
if  user_input == "1":
    pass
elif user_input == "2":
    pass
elif user_input == "3":
    pass
if __name__ == "__main__":
    main()

    
import schedule
import time
from datetime import datetime, timedelta

now = datetime.now()
after = datetime.now() + timedelta(minutes=1)

print(now < after)


def task():
    print("Task is running every 5 minutes.")


# Schedule the task to run every 5 minutes
schedule.every(1).minutes.do(task)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
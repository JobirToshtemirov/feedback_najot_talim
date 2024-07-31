from register_login import Renthouse, register, login, logout_all
from renthouse import
# method show menu for users 
def main_menu():
    menu = """
1. register
2. login
3. logout
"""
    print(menu)
    try:
        user_input = input("tanlang: ")
        if user_input == "1":
            register()
        elif user_input == "2":
            login()
        elif user_input == "3":
            logout_all()
            print("xayr ! ")
        else:
            print("notogri tanlov ! Qayta urinib koring. ")
            main_menu()
    except ValueError:
        print("Iltimos menudan birortasini tanlang. ")
        main_menu()

# method show admin menu for admin
def rent_menu():
    menu = """
    1. show all rent houses
    2. rent house
    3. search with room quantity
    4. search with city name
    5. application
    6. my rented houses
    7. delete my house
    8. my applications
    9. exit main menu
"""
    print(menu)
    try:
        user_input = input("tanlang: ")
        if user_input == "1":
            pass
        elif user_input == "2":
            rent_house()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        elif user_input == "5":
            pass
        elif user_input == "6":
            pass
        elif user_input == "7":
            pass
        elif user_input == "8":
            pass
        elif user_input == "9":
            pass
        else:
            print("notogri tanlov qayta urinib koring.")
            rent_menu()
    except ValueError:
        print("iltimos munu dan birortasini tanlang.")
        rent_menu()

if __name__ == "__main__":
    main_menu()

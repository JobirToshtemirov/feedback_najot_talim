from users import logout_all
from users import register, login
from announcement import add_announcement_as_taxi


def show_menu():
    text = """
    1. Add announcement as a taxi: 
    2. Add announcement as a client: 
    3. Filter taxis:
    4. Filter clients:
    5. Show my announcements: 
    6. Logout
"""
    print(text)

    user_input = input("Enter your choice: ")
    if user_input == "1":
        if not add_announcement_as_taxi():
            print("Something went wrong. Please try again.")
        show_menu()
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
        if login():
            show_menu()
        else:
            show_auth_menu()

    elif user_input == "3":
        print("Good bye !")
        return
    else:
        print("Wrong choice !")
        return show_auth_menu()


if __name__ == "__main__":
    logout_all()
    show_auth_menu()



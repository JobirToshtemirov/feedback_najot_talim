"""
O'tgan safar uyga berilgan kursga ro'yxatdan o'tish programmasini fayllar bilan ishlash orqali o'zgartirish:
1. Barcha kurslar haqidagi malumotlar courses.json nomli faylni ichida bo'lishi kerak
2. Foydalanuvchi ro'yxatdan o'tgan kurslar haqidagi malumotlar esa users.json faylni ichida bo'lishi kerak

"""

import json, os

coursess = dict()

def add_courses():
    course_name =input("Enter the course name : ")
    if course_name in coursess.keys():
        print("This course already exists")
        return add_courses()
    else:
         coursess[course_name] = {
              'course_name': course_name
        }
         save_data_to_json()
         return show_menu()

coursess = {}

def self_registered_course():
    course_name = input("Enter course name: ")
    full_name = input("Enter the full name: ")

    if course_name not in coursess:
        coursess[course_name] = {}

    if full_name in coursess[course_name]:
        print("This user already exists")
    else:
        phone_number = input("Enter the phone number: ")
        coursess[course_name][full_name] = phone_number
        save_data_to_json()
        show_text = f"{course_name}:\t {full_name}"
        print(show_text)
        print("Registration successful")

    return show_menu()

def show_self_registered_courses():
    user_full_name = input("Enter the full name: ")

    found_courses = []
    for course_name, students in coursess.items():
        if user_full_name in students:
            found_courses.append(course_name)

    if found_courses:
        print(f"User '{user_full_name}' is registered in the following courses: {found_courses}")
    else:
        print(f"User '{user_full_name}' is not registered in any courses.")
    
    return show_menu()

def save_data_to_json():
    file_path = 'Jobirt/coursess.json'
    with open(file_path, 'w') as file:
        json.dump(coursess, file, indent=4)

def load_data_from_json():
    global coursess
    file_path = 'Jobirt/coursess.json'
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            coursess = json.load(file)
    else:
        coursess = {}

def show_menu():
    text = """

1. Add new course 
2. Show all coursess
3. Registration| Subjects: Full_name, phone_number
4. View a list of self-registered courses
5. Exit

"""

    print(text)
    user_input = int(input("Choose from menu: "))
    if user_input == 1:
        add_courses()
    elif user_input == 2:
        for user in coursess.items():
            show_text = f"{user[0]}:\t {user[1]}"
            print(show_text)
            return show_menu()
    
    elif user_input == 3:
        self_registered_course()
        pass
    elif user_input == 4:
        show_self_registered_courses()
        pass
    elif user_input == 5:
        pass
    else:
        print("Good bye !")
        return
    
load_data_from_json()
show_menu()

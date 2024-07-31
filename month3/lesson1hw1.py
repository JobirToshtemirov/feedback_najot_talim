# h/w topshiriq

""" Terminalda ishlaydigan kalkulator yasash kerak,
 barcha nstijalarni faylda saqlab ketish kerak,
 va try exceptlardan foydalanish kerak, 
 unda quyidagi imkoniyatlari bo'lishi kerak. 
 Menu: 
 1. 2 ta sonni qo'shish: 
 2. 2 ta sonni ayirish: 
 3. 2 ta sonni bo'lish: 
 4. 2 ta sonni ko'paytirish 
 5. Darajaga oshirish: son, daraja 
 6. Barcha natijalarni ko'rish: 
 7. Barcha natijalarni amal bo'yicha ko'rish: 
 (yani odam 7 ni kiritsa siz unda qaysi amal bilan bajarilgan ishlarni ko'rmoqchi ekanligini so'raysiz 
  u amalni kiritadi va shu amal bilan bajarilgan ishlanri ro'yxatini ko'rsatasiz) 
 8. Barcha natijalarni o'chirish: 
 9. Chiqish """

# hw/natija or yechim


import os.path
import json
all_data=dict()
def read_func():
   if os.path.exists('data.json'):
      with open('data.json') as file:
         data=json.load(file)
         return data

def son_qoshish(all_data):
 try:

    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    plus="+"

    result = first_input+second_input
    print(f"First number: {first_input} plus to  second number: {second_input} is {result}")
    all_data[plus] = {
            'first_input': first_input,
            'second_input': second_input,
            'result': result
        }

    save_data_to_json(all_data)
    return show_menu()
 
 
 except Exception as xato:
  print(f"Invalid input {xato}" )
 return son_qoshish(all_data)


       
def son_ayirish(all_data):
 try:

    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    minus="-"

    result = first_input-second_input
    print(f"First number: {first_input} minus second number: {second_input} is {result}")
    all_data[minus] = {
            'first_input': first_input,
            'second_input': second_input,
            'result': result
        }

    save_data_to_json(all_data)
    return show_menu()
 
 
 except Exception as xato:
  print(f"Invalid input {xato}" )
 return son_ayirish(all_data)

def son_bolish(all_data):
 try:

    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    devide ="/"

    result = first_input/second_input
    print(f"First number: {first_input} devide to second number: {second_input} is {result}")
    all_data[devide] = {
            'first_input': first_input,
            'second_input': second_input,
            'result': result
        }

    save_data_to_json(all_data)
    return show_menu()
 
 
 except ValueError:
  print("Iltimos raqam kiriting !")
 except ZeroDivisionError: 
  print("har qanday sondi nolga bolish mumkun emas !")
 return son_bolish(all_data)

def son_kopaytirish(all_data):
 try:

    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    multiply="*"

    result = first_input*second_input
    print(f"First number: {first_input} mulitpy to second number: {second_input} is {result}")
    all_data[multiply] = {
            'first_input': first_input,
            'second_input': second_input,
            'result': result
        }

    save_data_to_json(all_data)
    return show_menu()
 
 
 except Exception as xato:
  print(f"Invalid input {xato}" )
 return son_kopaytirish(all_data)


def darajaga_oshirish(all_data):
 try:

    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the number of degree: "))
    degree="**"

    result = first_input**second_input
    print(f"First number: {first_input}  degree to second number: {second_input} is {result}")
    all_data[degree] = {
            'first_input': first_input,
            'second_input': second_input,
            'result': result
        }

    save_data_to_json(all_data)
    return show_menu()
 
 
 except Exception as xato:
  print(f"Invalid input {xato}" )
 return darajaga_oshirish(all_data)


def show_all_data(all_data):
    if not all_data:
        print("No data found.")
    else:
        for phone_number, details in all_data.items():
            show_text = f"{phone_number}: {details}"
            print(show_text)
    return show_menu()

def show_all_data_with_action(all_data):
    user_action = input("Enter the action plus/minus/devide/multiply/degree ")
    if user_action in ['plus','minus','devide','multiply','degree']:
       print(read_func())
    else:
       print(False)
    # for all_data, details in all_data.keys():
        
    #         show_text = f"{user_action}: {details}"
    #         print(show_text)
    #         return show_menu()

def delete_all_data(all_data):
    all_data.clear()
    save_data_to_json(all_data)
    print("All data have been deleted.")
    return show_menu()


       


def save_data_to_json(all_data):
    with open("data.json", 'w') as file:
          json.dump(all_data, file, indent=4)


def load_data_from_json():
    file_path = 'data.json'
    if os.path.exists(file_path):
        with open("data.json", 'a') as file:
         with open(file_path, 'r') as file:
            all_data = json.load(file)
    else:
        all_data = {}
        return all_data
    
def show_menu():
 try:
    text = """
 1. 2 ta sonni qo'shish: 
 2. 2 ta sonni ayirish: 
 3. 2 ta sonni bo'lish: 
 4. 2 ta sonni ko'paytirish 
 5. Darajaga oshirish: son, daraja 
 6. Barcha natijalarni ko'rish: 
 7. Barcha natijalarni amal bo'yicha ko'rish: 
 (yani odam 7 ni kiritsa siz unda qaysi amal bilan bajarilgan ishlarni ko'rmoqchi ekanligini so'raysiz 
  u amalni kiritadi va shu amal bilan bajarilgan ishlanri ro'yxatini ko'rsatasiz) 
 8. Barcha natijalarni o'chirish: 
 9. Chiqish """
    
    print(text)

    user_input = int(input("Enter your choice: "))
    if user_input == 1:
      son_qoshish(all_data)
    elif user_input == 2:
      son_ayirish(all_data)
    elif user_input == 3:
      son_bolish(all_data)
    elif user_input == 4:
        son_kopaytirish(all_data)
    elif user_input == 5:
       darajaga_oshirish(all_data)
    elif user_input == 6:
       show_all_data(all_data)
    elif user_input == 7:
       show_all_data_with_action(all_data)
    elif user_input == 8:
       delete_all_data(all_data)
    elif user_input == 9:
        print("Good bye !")   
    else:
         print("Good bye !")
         return
    
 except Exception as xatocha:
    print(xatocha)
    print("1 dan 9 gacha bolgan sonlarni kiriting")
    return show_menu()

if __name__ == "__main__":
    show_menu()




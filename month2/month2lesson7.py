# import os 
# Subject_name=input("Enter your Subject and mark: ")
# if os.path.exists(Subject_name + '.txt'):
#         print("Mavjud: ")
# else:
#         new_file = open(Subject_name + '.txt', 'x' )
#         new_file.close()

import os

def show_menu():
 text = """
    1: Papka yaratish | ism
    2: Fan bahosini qo'shish | ism, fan nomi, bahosi
    3: Bahosini yangilash: | ism, fan nomi, yangi baho
    4. Fanni o'chirish: | ism, fan nomi
    5. Papkani o'chirish: | ism
    """
 print(text)
 user_input = input("Enter: ")
 if user_input==1:
    if os.path.exists(user_input):
     print("bor")
 else:
    os.mkdir('Jobirt')
    user_input = input("Enter: ")
    return show_menu
 if user_input==2:
  
  if os.path.exists(user_input + '.txt'):
        print("Mavjud: ")
 else:
        new_file = open(user_input + '.txt', 'x' )
        new_file = open(user_input + 'txt', 'a')
        new_file.close()







show_menu()
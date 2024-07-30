# # hw/8

# """ Karta yaratish va unga pul tashlash uchun dastur Unda quyidagi imkoniyatlar bo'lishi kerak: 
# 1: Yangi karta sotib olish | passport_number, full_name, password 
# 2: Kartasiga pul tashlash | card_number, password, money 
# 3: Kartasidagi malumotlarni ko'rish | card_number, password 
# 4: Exit
# cards.json | kartalarni malumotini saqlash uchun 
# transfers.json | o'tkazmalarni ro'yxatini saqlash uchun  """


# import json, os, random

# cards = dict()

# def buy_card():
#     card_number =(random.randint(8600000000000000,8600999999999999))
#     passport_number =input("Enter your passport number : ")
#     full_name =input("Enter your full_name  : ")
#     password =input("Enter your password  : ")

#     cards[card_number] = {
#               'full_name': full_name,
#               'passport_number': passport_number,
#               'password': password,
#         }
#     save_data_to_json()
#     return show_menu()

# def append_money():
#     user_card_number = input("Enter the card number: ")
#     user_password_number = input("Enter the password: ")

#     found_card = []
#     for cards, user_card_number in cards():
#          if user_card_number in cards:
#             user_money=print(input("Enter money "))
#             found_card.append(user_money)


#             print(f"{user_card_number} : {user_password_number}': {user_money}")
#     else:
#         print(f"The card '{user_card_number}' is not bought.")
    
#     return show_menu()

# def user_card ():
#    users_card = print(input("Enter your card number: "))
#    for user in cards:
#     if user_card in cards.items():
#      show_text = f"{user[0]}:\t {user[1]}"
#      print(show_text)

# def save_data_to_json():
#     file_path = 'hw8/cards.json'
#     with open(file_path, 'a') as file:
#         with open(file_path, 'r+') as file:
#          json.dump(cards, file, indent=4)

# def show_menu():
#     text = """

# 1: Yangi karta sotib olish | passport_number, passport_number, password 
# 2: Kartasiga pul tashlash | card_number, password, money 
# 3: Kartasidagi malumotlarni ko'rish | card_number, password 
# 4: Exit

# """

#     print(text)
#     user_input = int(input("Choose from menu: "))
#     if user_input == 1:
#         buy_card()
#     elif user_input == 2:
#         append_money()
#         return show_menu()
#     elif user_input == 3:
#         user_card()
#         return show_menu()
#     elif user_input == 4:
#         print("Good bye !")
#     return
# show_menu()
# a = print(input("enter name"),
#           ("Enter age"))


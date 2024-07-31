# employess = dict()

# def add_employes():
#     user_id =input("Enter the id employess: ")
#     full_name = input("Enter the full_name: ")
#     if user_id in employess.keys():
#         print("This employes already exists")
#         return add_employes()
#     else:       
#         phone_number = int(input('Enter phone_number: '))
#         salary = int(input('Enter salary: '))
#         position = (input('Enter position: '))

#         employess[user_id] = {
#             'full_name': full_name,
#             'phone_number': phone_number,
#             'salary': salary,
#             'position': position
#         }
#         return show_menu()
    
        

# # def show_menu():
# #     text = """
# # 1. Add new employes | Subjects:  id, full_name, phone_number, position, salary
# # 2. Show all employess
# # 3. Search employes with full_name
# # 4. Delete employes with id
# # 5. Exit

# # """
# def search_employess():
#     user_full_name = input("Enter the full_name: ")
    
#     for user_id, details in employess.items():
#         if details['full_name'] == user_full_name:
#             show_text = f"{user_id}:\t {details}"
#             print(show_text)

# def remove_employes_with_id(employess,user_id):
#     user_id =input("Enter the id employess")

#     for user_id, deleted_name in employess:
#         if deleted_name['user_id'] == user_id:
#            del(user_id)
#            show_text=f"{user_id}:\t {deleted_name}"
#            print(show_text)
#     return show_menu()

# def show_menu():
#     text = """
# 1. Add new employes | Subjects:  id, full_name, phone_number, position, salary
# 2. Show all employess
# 3. Search employes with full_name
# 4. Delete employes with id
# 5. Exit

# """

#     print(text)
#     user_input = int(input("Choose from menu: "))
#     if user_input == 1:
#         add_employes()
#     elif user_input == 2:
#         for user in employess.items():
#             show_text = f"{user[0]}:\t {user[1]}"
#             print(show_text)
#         return show_menu()
    
#     elif user_input == 3:
#         search_employess()
#         pass
#     elif user_input == 4:
#         remove_employes_with_id()
#         pass
#     elif user_input == 5:
#         pass
#     else:
#         print("Good bye !")
#         return


# show_menu()

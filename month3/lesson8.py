# import hashlib
# from abc import ABC, abstractmethod
# import json

# class FileManager:
#     def __init__(self):
#         self.file_name = 'hashlib.json' 

#     def read_file(self):
#         try:
#             with open(self.file_name, 'r') as f:
#                 return json.load(f)
#         except FileNotFoundError:
#             with open(self.file_name, 'w') as f:
#                 json.dump([], f)
#                 return []

#     def write_file(self, data):
#         with open(self.file_name, 'w') as f:
#             json.dump(data, f, indent=4)
#             return True

#     def add_result(self, result):
#         data = self.read_file()
#         data.append(result)
#         self.write_file(data)


# class Najottalim(FileManager):

#     def __init__(self, full_name, studenrt_id,password, ):
#         self.full_name = full_name
#         self.id = studenrt_id
#         self.all_users = []
#         password = "buguun quyosh"

#         hashed_password = hashlib.sha256(password.encode()).hexdigest()
#         print(hashed_password)
        
#     def register(self, full_name,id,password ):
#         result_read = self.read_file()
#         result_read.append(f"full_name: { full_name} id: {id} password: {password}": False)
#         super().write_file(data=result_read)
#         print(f'user added: {full_name}')


#     def login (self):
#         result_read = self.read_file()
#         for user in result_read:
#             if user in result_read:
#                 print(f'user name: {user["name"]},user id l: {user["id"]}, user password: {user["password"]}')
#         return True
        
    
    



#     def add_product(self, name, price,quantity):
#         self.file_name= input("input name")
#         self.price =input("input price")
#         self.quantity = input("input quantity ")

#         result_read = self.read_file()
#         result_read.append({'name': name, 'price': price, 'quantity': quantity: })
#         super().write_file(data=result_read)
#         print(f'product added: {name}')
#         return show_menu()
     

    # def delete_product(self, product_name):
    #     result_read = self.read_file()
    #     isThere = False
    #     if len(result_read) == 0:
    #         print('No product found')
    #         return show_menu()
    #     try:
    #         for product in result_read:
    #             if product["name"].lower() == product_name.lower():
    #                 isThere = True
    #                 if product['is deleted']:
    #                     print('The product is already deleted, please choose another product')
    #                 else:
    #                     print('You deleted a product')
    #                     product['is deleted'] = True
    #                 break
    #         if not isThere:
    #             print('The product is not deleted, please choose another product')
    #         self.write_file(result_read)
    #     except IndexError:
    #         print("Not found products")
    #     return show_menu()
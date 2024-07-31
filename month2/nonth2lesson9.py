# # file= open(file="names.txt", mode="w", encoding="utf-8")

# # file.write("Алекс")
# # file.close()
with open(file="users.csv", mode="w", encoding="UTF-8") as file:
    file.write("#,number,Name,Age\nAlex,25\nJobir ,21\nJasur,25")


# def user():
#   with open(file="users.csv", mode="w", encoding="UTF-8") as file:
#          file.write("#,Name,Age\n") 
#          file.write(f"{name},{age}\n")
# while True:
#         name = input("Enter your name: ")
#         age = input("Enter your age: ")
#         if name == "exit" or age  == "exit":
        
#               print("Dastur yakunlandi")
#               break
# user()




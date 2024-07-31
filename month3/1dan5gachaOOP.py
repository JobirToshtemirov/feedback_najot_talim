# # # day 1 task1

# # class Amal:
# #     def __init__(self,num1, num2, num3):
# #         self.num1 = num1
# #         self.num2 = num2
# #         self.num3 = num3

# #     def qoshish(self):
# #         return f"{self.num1 + self.num2 + self.num3}"
    
# #     def ayrish(self):
# #         return f"{self.num1 - self.num2 - self.num3}"
    
# #     def bolish(self):
# #         return f"{self.num1 * self.num2 * self.num3}"
    
# #     def kopayt(self):
# #         return f"{self.num1 / self.num2 / self.num3}"
    
# # number = Amal(5,10,2)

# # print(number.qoshish())
# # print(number.ayrish())
# # print(number.bolish())
# # print(number.kopayt())




# # day 3task 1 

# """
# Jamoa bo'lib bajarish mumkin: 
# Classes: Student, Course, Teacher
# Student Variables: name, email, phone_number, id 
# Methods: - register - get_info - delete_account - get_registered_courses - register_to_course 
# Teacher Variables: name, phone_number, profession, age 
# Methods: - add_to_file - get_info - delete_course - get_registered_users 
# Course Variables: name, price, 
# Course Methods: - add_to_file - get_info - delete_course - get_registered_users 

# Menu: 
# 1. Create a new teacher: name, phone_number, profession, age 
# 2. Crate a course: name, price, teacher_phone_number 
# 3. Register to course: name, email, phone_number, id 
# 4: Delete a course: name 
# 5: Delete a teacher: phone_number 
# 6: Get registered courses: phone_number 
# 7. Get users by course: course_name 
# 8. Exit

# """
# # Fatrher class education
# class Education:
#     def __init__(self, name, phone_number):
#         self.name = name
#         self.phone_number = phone_number


# #  class teachers info  and methods

# class Teachers(Education):
#     def __init__(self,name, phone_number, profession, age):
#         super().__init__(name,phone_number)

#         self.profession = profession
#         self.age = age 

#     def add_to_file():
#         pass
#     def get_info():
        
#         return f"name{name} phone number{phone_number} profession{profession} age{age}"
        
#     def delete_course():
#         pass
#     def get_register_course():
#         pass
    
#     def new_teacher():
#         name = input("Enter your name: ")
#         phone_number =  input("Enter your phone number: ")
#         profession =  input("Enter your profession: ")
#         age =  input("Enter your age: ")
#         return "Teacher added succesfully "

# #  class student info  and methods

# class Student(Education):
#     def __init__(self, name, email, phone_number, id) -> None:
#         super().__init__(name, phone_number)
#         self.email = email
#         self.id = id

#         Methods: - register - get_info - delete_account - get_registered_courses - register_to_course 

#     def register():
#         name = input("Enter your name: ")
#         email = input("Enter your email adress: ")
#         phone_number = input("Enter your phone number: ")
#         id = input("Enter your id: ")
#     register()




# class Course(Education):
#     def __init__(self, name, phone_number,  teacher_phone_number, price ):
#         super().__init__(name, phone_number)
#         self.price = price


#         Course Methods: - add_to_file - get_info - delete_course - get_registered_users 


#     def new_cource():
#         name = input("Enter the course  name: ")
#         price = input("Enter the course price: ")
#         teacher_phone_number = input("Enterthe teachers phone number: ")

# tugatish kerak tugatilmagan 

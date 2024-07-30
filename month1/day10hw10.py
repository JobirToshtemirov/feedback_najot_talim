# task1
 
# a = input("enter the number: ")
# b = input("enter the desired number: " )
# desired_number = b
# count = 0
# for ele in a:
#     if(ele==(b)):
#         count=count+1
#         print("{} has occured {}times". format (desired_number,count))

#  task 2

# m = int(input("Enter the  distance in mm: ")) # o'zgartiruvchi ochib uni kiritiladigan songa tenglab olamiz
# print("in km: ", m *0.000001) #va shunchaki print orqali km m sm larga o'zgarishi uchun uni belgilangan metr sistemasi orqali kopaytirib qoyamiz 
# print("in m: ", m *0.001)
# print("in dm: ", m *0.01)
# print("in sm: ", m *0.1)

# # task3

# def count_divisors(num):
#     count = 0
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             count += 1
#             if i != num // i:
#                 count += 1
#     return count

# def find_numbers_with_5_divisors(start, end):
#     return [num for num in range(start, end + 1) if count_divisors(num) == 5]

# numbers_with_5_divisors = find_numbers_with_5_divisors(1, 1000)
# print("Numbers with 5 divisors in the range 1 to 1000:", numbers_with_5_divisors)



# task 4

# multiplication numbers  #karra jadvali
# for a in range(1,10):   # o'zgaruvchini nechidan nechigacha ishlashi 
#     print("Muliplication Table: of %d is  " %a)   # va bu yerda printga chaqirib olamiz

#     for b in range(1,11):     #bu yerdaham o'zgaruvchini nechidan nechigacha ishlashi 
#      print(a," * ",b, " = ", a*b)    # Bu yerda nimani print qilish kerak ligini  berib qoyamiz 

# task 5

# palindrome = input("please enter the value: ")    # biror soz yoki nom kiritishni soraymiz

# reverse = palindrome[::-1]    # kiritilgan son yoki nomni teskari oqib olamiz

# if (palindrome==reverse): # agar kiritilgan son yoki nom yeskarisiga teng bolsa print qilsin 
#     print("Yes it is palindrome: ", palindrome)
# else: # agar kiritilgan son yoki nom teskarisiga teng bolmasa print qilsin  
#     print("No it is not palindrome: ", palindrome)



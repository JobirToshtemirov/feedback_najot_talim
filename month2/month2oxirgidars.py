user = input("enter first number: ")
user2 = input("enter second number: ")
count=0
while user>=user2:
    if user2<user:
        user2+user2
        count+=1
    else:
     print("birinchi son katta bolsin")
print(count)
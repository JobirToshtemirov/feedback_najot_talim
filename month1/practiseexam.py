# task4 1 korinishi
# def a (sekunds):
#     kun = sekunds//(24*3600)
#     sekunds%=(24*3600)
#     soat = sekunds//3600
#     sekunds%=3600
#     minut = sekunds//60
#     sekunds%=60
     
#     return kun,soat,minut,sekunds
# b=int(input("sekundlarni kiriting: "))
# kun= a(b)
# soat= a(b)
# kun= a(b)
# minut= a(b)
# sekunds= a(b)
# print(f"{b} sekund bu: =  ({b}")
# print(f"{kun}days")
# print(f"{soat} hours" )
# print(f"{minut} minutes") 
# print(f"{sekunds} seconds")

# task4 2 korinishi

def a (sekunds):
    yil =sekunds//(365*86400)
    sekunds%=(365*86400)
    kun = sekunds//(24*3600)
    sekunds%=(24*3600)
    soat = sekunds//3600
    sekunds%=3600
    minut = sekunds//60
    sekunds%=60
    return  yil,kun,soat,minut,sekunds
b=int(input("sekundlarni kiriting: "))
yil,kun,soat,minut,sekunds= a(b)
print(f"{b} sekund bu: =  ({b}")
print(f"{yil}years")
print(f"{kun}days")
print(f"{soat} hours" )
print(f"{minut} minutes") 
print(f"{sekunds} seconds")



  # hw5
"""
Ovqat zakaz qilish uchun terminalda ishlaydigan dastur tuzish kerak: 
Uni quyidagi imkoniyatlari bo'lishi kerak: 

0. Oshxona va ovqatlarini qo'shish:
1. Hamma oshxonalarni ko'rish: 
2. Biror bir oshxonani nomi bo'yicha uni hamma ovqatlarini ko'rish:
3. Taom ni nomi bo'yicha qidirish:
4. Biror bir oshxonani nomi bo'yicha o'chirish: 
5. Chiqish
"""

choyhonalar = {
    'ulfatlar': {
        'osh': 220000,
        'shashlik': 22000,
        'tandir kabob': 40000,
        'limon choy': 10000
    },
    'sadacha': {
        'mastava': 25000,
        'tandir kabob': 40000,
        'qozon kabob': 40000,
        'suv': 3500
    },
    'maxdum ota': {
        'osh': 250000,
        'mastava': 40000,
        'tandir kabob': 40000,
        'limon choy': 3000
    },
    'dostlar': {
        'qozon kabob': 37000,
        'tandir kabob': 40000,
        'osh': 235000,
        'kampot': 4000
    }
}

def Add_kitchens_and_foods():
    kitchen_name = input("Enter the kitchen name: ")
    if kitchen_name in choyhonalar:
        print("This kitchen already exists")
        return Add_kitchens_and_foods()
    else:
        foods = {}
        for i in range(3):  
            food_name = input(f'Enter food name {i + 1}: ')
            food_price = int(input(f'Enter price for {food_name}: '))
            foods[food_name] = food_price
        water_name = input('Enter water name: ')
        water_price = int(input(f'Enter price for {water_name}: '))
        foods[water_name] = water_price

        choyhonalar[kitchen_name] = foods
        return show_menu()

def Search_food_with_name():
    food_name = input("Enter the food name: ")
    found = False
    for kitchen_name, foods in choyhonalar.items():
        if food_name in foods:
            show_text = f"{kitchen_name}:\t {food_name}: {foods[food_name]}"
            print(show_text)
            found = True
    if not found:
        print("No food found with that name")


def Delete_kitchen_with_name():
    kitchen_name = input("Enter the kitchen name to delete: ")
    if kitchen_name in choyhonalar:
        deleted_kitchen = choyhonalar.pop(kitchen_name)
        print(f"Deleted {kitchen_name}: {deleted_kitchen}")
    else:
        print("No kitchen found with that name")
    return show_menu()

def show_menu():
    text = """
    0. Add kitchens and foods:
    1. View all kitchens: 
    2. View all foods with kitchen name:
    3. Delete kitchen with name: 
    4. Search food with name: 
    5. Exit: 
    """
    print(text)
    user_input = int(input("Choose from menu: "))
    if user_input == 0:
        Add_kitchens_and_foods()
    elif user_input == 1:
        for kitchen_name, kitchen_foods in choyhonalar.items():
            show_text = f"{kitchen_name}:\t {kitchen_foods}"
            print(show_text)
        return show_menu()
    elif user_input == 2:
        kitchen_name = input("Enter the kitchen name: ")
        if kitchen_name in choyhonalar:
            kitchen_foods = choyhonalar[kitchen_name]
            show_text = f"{kitchen_name}:\t {kitchen_foods}"
            print(show_text)
        else:
            print("No kitchen found with that name")
        return show_menu()
    elif user_input == 3:
        Delete_kitchen_with_name()
    elif user_input == 4:
        Search_food_with_name()
    elif user_input == 5:
        print("Goodbye!")
    else:
        print("Invalid choice, try again.")
        return show_menu()

show_menu()

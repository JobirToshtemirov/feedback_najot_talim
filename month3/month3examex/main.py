from registerlogin import RegisterLogin
from renthouse import RentHouse

def main_menu():
    user_manager = RegisterLogin('month3/month3examex/data/users.json')
    house_manager = RentHouse('month3/month3examex/data/houses.json')
    current_user = None

    while True:
        if current_user:
            print("\nRent Menu:")
            print("1. Show all rent houses")
            print("2. Rent house")
            print("3. Search with room quantity")
            print("4. Search house with city name")
            print("5. Add comment to house")
            print("6. My rented houses")
            print("7. Delete my house")
            print("8. My comments")
            print("9. Add house")
            print("10. Logout")

            choice = input("Choose an option: ")

            if choice == '1':
                house_manager.show_all_houses()
            elif choice == '2':
                house_id = int(input("Enter house ID to rent: "))
                house_manager.rent_house(current_user, house_id)
            elif choice == '3':
                rooms = int(input("Enter room quantity: "))
                houses = house_manager.search_by_rooms(rooms)
                for house in houses:
                    print(house)
            elif choice == '4':
                city = input("Enter city name: ")
                houses = house_manager.search_by_city(city)
                for house in houses:
                    print(house)
            elif choice == '5':
                house_id = int(input("Enter house ID to comment on: "))
                comment = input("Enter your comment: ")
                if house_manager.add_comment(current_user, house_id, comment):
                    print("Comment added successfully.")
            elif choice == '6':
                print("My rented houses:", current_user['houses'])
            elif choice == '7':
                house_id = int(input("Enter house ID to delete: "))
                house_manager.delete_house(current_user, house_id)
            elif choice == '8':
                comments = house_manager.get_user_comments(current_user['username'])
                for comment in comments:
                    print(comment)
            elif choice == '9':
                city = input("Enter city: ")
                rooms = int(input("Enter number of rooms: "))
                rent = (input("Enter rent amount: "))
                house_manager.add_house(current_user, city, rooms, rent)
                print("House added successfully.")
            elif choice == '10':
                current_user = user_manager.logout(current_user)
        else:
            print("\nMain Menu:")
            print("1. Register")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if user_manager.register(username, password):
                    print("Registration successful.")
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                current_user = user_manager.login(username, password)
                if current_user:
                    print("Login successful.")
            elif choice == '3':
                break

if __name__ == '__main__':
    main_menu()

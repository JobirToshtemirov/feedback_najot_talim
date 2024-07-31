from filemanager import FileManager
from admin import Admin
from users import User

def main():
    file_manager = FileManager()
    admin = Admin(file_manager)
    user = User(file_manager)
    
    def admin_login():
        password = input("Enter admin password: ")
        stored_password = file_manager.get_data('admin_password')
        return password == stored_password

    while True:
        print("1. Rent scooter")
        print("2. Return scooter")
        print("3. Show all scooters")
        print("4. Admin menu")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            scooter_id = input("Enter scooter ID: ")
            user_name = input("Enter your name: ")
            if user.rent_scooter(scooter_id, user_name):
                print("Scooter rented successfully!")
            else:
                print("Scooter is not available.")

        elif choice == '2':
            scooter_id = input("Enter scooter ID: ")
            cost = user.return_scooter(scooter_id)
            if cost is not None:
                print(f"Scooter returned successfully! Total cost: ${cost:.2f}")
            else:
                print("Scooter was not rented or invalid ID.")

        elif choice == '3':
            scooters = user.show_all_scooters()
            if scooters:
                for scooter_id, scooter_info in scooters.items():
                    print(f"ID: {scooter_id}, Charge: {scooter_info['charge']}, Location: {scooter_info['location']}, Price per minute: {scooter_info['price_per_minute']}, Rented: {'Yes' if scooter_info['rented'] else 'No'}")
            else:
                print("No scooters available.")

        elif choice == '4':
            if admin_login():
                while True:
                    print("Admin menu:")
                    print("1. Add scooter")
                    print("2. Delete scooter")
                    print("3. Exit to main menu")

                    admin_choice = input("Choose an option: ")

                    if admin_choice == '1':
                        charge = input("Enter charge level: ")
                        location = input("Enter location: ")
                        price_per_minute = input("Enter price per minute: ")
                        scooter_id = admin.add_scooter(charge, location, price_per_minute)
                        print(f"Scooter added successfully with ID: {scooter_id}")

                    elif admin_choice == '2':
                        scooter_id = input("Enter scooter ID to delete: ")
                        admin.delete_scooter(scooter_id)
                        print("Scooter deleted successfully.")

                    elif admin_choice == '3':
                        break
            else:
                print("Invalid password!")

        elif choice == '5':
            break

if __name__ == "__main__":
    main()

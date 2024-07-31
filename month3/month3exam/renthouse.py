from filemanager import FileManager, filemanager
from main import rent_menu



class Renthuse:
    def __init__(self,house_number, house_city,):
        self.house_number = house_number
        self.house_city = house_city 
def show_teams(self,house_city):
    houses = FileManager.read_json_file()
    if house:
        for house_number, house in houses:
            print(f"house: {house_city} house number: {house_number} ")
    else:
        print("bunday uy yoq.")
    return rent_menu()

def rent_house(self, house_number, user_name):
        houses = self.filemanager.get_data('houses')
        house = houses.get(house_number)
        if house and not houses['rented']:
            house['rented'] = True
            house['user'] = user_name
            houses[house_number] = house
            self.filemanager.update_data('houses', houses)
            return True
        return False

def submit_application(house_city,house_number):
    house_city = input("shahar nomini kiritng: ")
    house_number = input("uyni raqaminii kiritng: ")
    user_koment = input("Maqsadingizni yozib qoldiring")
    houses = []
    houses.append(house_city,house_number,user_koment)
    
def delete_house():
    houses = filemanager.read_json_file()
    if house:
        for house_number, house in houses:
            print(f" house_number: {house_number}")
        try:
            house_number = int(input("ochirish uchun uy raqamini kiriting: ")) 
            if 0 <= house_number < len(houses):
                houses.pop(house_number)
                filemanager.write_to_json(houses)
                print("uy muovfaqiyatli ochirildi.")
            else:
                print("notogri uy raqami.")
        except ValueError:
            print("iltimos uyning togri raqamini kiriting.")
    else:
        print("uy topilmadi.")
    return rent_menu()



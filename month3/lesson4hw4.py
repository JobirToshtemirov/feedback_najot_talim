import json


class FileManager:
    def __init__(self):
        self.file_name = 'data.json'

    def read_file(self):
        try:
            with open(self.file_name, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            with open(self.file_name, 'w') as f:
                json.dump([], f)
                return []

    def write_file(self, data):
        with open(self.file_name, 'w') as f:
            json.dump(data, f, indent=4)
            return True


class RentCar(FileManager):
    def add_car(self, name, model):
        result_read = self.read_file()
        result_read.append({'name': name, 'model': model, 'in_rented': False})
        super().write_file(data=result_read)
        print(f'Car added: {name}')
        return show_menu()

    def get_all_cars(self):
        result_read = self.read_file()
        for car in result_read:
            print(f'Car name: {car["name"]}, car model: {car["model"]}')
        return True

    def rent_car(self, car_name):
        result_read = self.read_file()
        isThere = False
        if len(result_read) == 0:
            print('No car found')
            return show_menu()
        try:
            for car in result_read:
                if car["name"].lower() == car_name.lower():
                    isThere = True
                    if car['in_rented']:
                        print('The car is already rented, please choose another car')
                    else:
                        print('You rented a car')
                        car['in_rented'] = True
                    break
            if not isThere:
                print('The car is not rented, please choose another car')
            self.write_file(result_read)
        except IndexError:
            print("Not found cars")
        return show_menu()

    def return_rented_car(self):
        result_read = self.read_file()
        try:
            for car in result_read:
                car['in_rented'] = False
            self.write_file(result_read)
            print('The cars were returned')
        except IndexError:
            print("Not found cars")
        return show_menu()


def show_menu():
    text = '''
1. Add car
2. Rent
3. Return car
4. Exit    
    '''
    print(text)
    rentcar = RentCar()
    try:
        user_input = int(input('Enter your choice: '))
        if user_input == 1:
            user_car_name = input('Enter car name: ')
            user_car_model = input('Enter car model: ')
            rentcar.add_car(name=user_car_name, model=user_car_model)
        elif user_input == 2:
            rentcar.get_all_cars()
            user_car_name = input('Enter car name: ').strip()
            rentcar.rent_car(user_car_name)
        elif user_input == 3:
            rentcar.return_rented_car()
        else:
            print('Good bye!')
            return
    except ValueError:
        print('Please enter a number')
        show_menu()


if __name__ == '__main__':
    show_menu()
from filemanager import FileManager

class RentHouse:
    def __init__(self, house_file):
        self.file_manager = FileManager(house_file)

    def add_house(self, user, city, rooms, rent):
        houses = self.file_manager.read_data()
        house_id = len(houses) + 1
        house = {'id': house_id, 'owner': user['username'], 'city': city, 'rooms': rooms, 'rent': rent, 'rented': False, 'comments': []}
        houses.append(house)
        self.file_manager.write_data(houses)
        user['houses'].append(house_id)

    def show_all_houses(self):
        houses = self.file_manager.read_data()
        for house in houses:
            print(house)

    def search_by_rooms(self, rooms):
        houses = self.file_manager.read_data()
        result = [house for house in houses if house['rooms'] == rooms]
        return result

    def search_by_city(self, city):
        houses = self.file_manager.read_data()
        result = [house for house in houses if house['city'].lower() == city.lower()]
        return result

    def rent_house(self, user, house_id):
        houses = self.file_manager.read_data()
        for house in houses:
            if house['id'] == house_id and not house['rented']:
                house['rented'] = True
                self.file_manager.write_data(houses)
                user['houses'].append(house_id)
                return True
        print("House not available for rent.")
        return False

    def delete_house(self, user, house_id):
        houses = self.file_manager.read_data()
        houses = [house for house in houses if house['id'] != house_id or house['owner'] != user['username']]
        self.file_manager.write_data(houses)
        user['houses'].remove(house_id)

    def add_comment(self, user, house_id, comment):
        houses = self.file_manager.read_data()
        for house in houses:
            if house['id'] == house_id:
                house['comments'].append({'username': user['username'], 'comment': comment})
                self.file_manager.write_data(houses)
                return True
        print("House not found.")
        return False

    def get_user_comments(self, username):
        houses = self.file_manager.read_data()
        user_comments = []
        for house in houses:
            for comment in house['comments']:
                if comment['username'] == username:
                    user_comments.append({'house_id': house['id'], 'comment': comment['comment']})
        return user_comments


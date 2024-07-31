import random

class Admin:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def add_scooter(self, charge, location, price_per_minute):
        scooters = self.file_manager.get_data('scooters')
        scooter_id = str(random.randint(1, 99))
        scooter_info = {
            'charge': charge,
            'location': location,
            'price_per_minute': price_per_minute,
            'rented': False,
            'start_time': None,
            'end_time': None,
            'user': None
        }

        scooters[scooter_id] = scooter_info
        self.file_manager.update_data('scooters', scooters)
        return scooter_id

    def delete_scooter(self, scooter_id):
        scooters = self.file_manager.get_data('scooters')
        if scooter_id in scooters:
            del scooters[scooter_id]
            self.file_manager.update_data('scooters', scooters)

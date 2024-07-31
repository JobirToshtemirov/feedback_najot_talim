import time
class User:
    def __init__(self, file_manager):
        self.file_manager = file_manager

    def rent_scooter(self, scooter_id, user_name):
        scooters = self.file_manager.get_data('scooters')
        scooter = scooters.get(scooter_id)
        if scooter and not scooter['rented']:
            scooter['rented'] = True
            scooter['start_time'] = time.time()
            scooter['user'] = user_name
            scooters[scooter_id] = scooter
            self.file_manager.update_data('scooters', scooters)
            return True
        return False

    def return_scooter(self, scooter_id):
        scooters = self.file_manager.get_data('scooters')
        scooter = scooters.get(scooter_id)
        if scooter and scooter['rented']:
            scooter['end_time'] = time.time()
            scooter['rented'] = False
            usage_time = scooter['end_time'] - scooter['start_time']
            cost = int(usage_time / 60 * scooter['price_per_minute'])
            scooter['start_time'] = None
            scooter['end_time'] = None
            scooter['user'] = None
            scooters[scooter_id] = scooter
            self.file_manager.update_data('scooters', scooters)
            return cost
        return None

    def show_all_scooters(self):
        scooters = self.file_manager.get_data('scooters')
        return scooters

import random

##### Main Class #####
class SensorSystem:
    ##### Initializing #####
    def __init__(self):
        self.vehicle_at_entry = False
        self.vehicle_at_exit = False
        self.vehicle_list = []
        self.joined_plate = ""

    ##### Entry Triggered #####
    def entry_triggered(self):
        self.vehicle_at_entry = random.random() < 0.10
        return self.vehicle_at_entry

    ##### Exit Triggered #####
    def exit_triggered(self):
        self.vehicle_at_exit = random.random() < 0.05
        return self.vehicle_at_exit
    
    ##### Detect Vehicle Type #####
    def detect_vehicle_type(self):
        vehicle_type = ['Motorcycle', 'Car', 'SUV', 'Truck'] 
        random_vehicle = random.choice(vehicle_type)

        self.vehicle_list.append(random_vehicle)

        return random_vehicle
    
    def plate_generator(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"

        generate_plate = [random.choice(letters), random.choice(letters), random.choice(letters), random.choice(numbers), random.choice(numbers), random.choice(numbers), random.choice(numbers)]

        joined_plate = "".join(generate_plate)

        return joined_plate
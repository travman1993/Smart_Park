##### Main Class #####
class AnalyticsTracker:
    ##### Initializing #####
    def __init__(self):
        self.motorcycles = 0
        self.cars = 0
        self.suv = 0
        self.trucks = 0

        self.total = 0

    def register_vehicle(self, vehicle_type):
        if vehicle_type == "Motorcycle":
            self.motorcycles += 1
        
        elif vehicle_type == "Car":
            self.cars += 1

        elif vehicle_type == "SUV":
            self.suv += 1
        
        else:
            self.trucks += 1
        
        self.total += 1

        print(f"Total: {self.total}, Motorcyles: {self.motorcycles}, Cars: {self.cars}, SUV: {self.suv}, Trucks: {self.trucks}")

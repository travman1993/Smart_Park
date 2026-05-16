from datetime import datetime

# Main Class
class OccupancyManager:
    ##### Inizializing #####
    def __init__(self):
        # Variables
        self.max_capacity = 0
        self.current_occupancy = 0
        self.availible_spaces = 0

    ##### Availible spaces counter #####
    def get_availible_spaces(self):
        self.availible_spaces = (self.max_capacity - self.current_occupancy)
        return self.availible_spaces

    ##### Full Compacity #####
    def is_full(self):
        if self.current_occupancy >= self.max_capacity:
            return True
        return False

    ##### Vehicle Entered #####
    def vehicle_entered(self):
        self.current_occupancy += 1    
    
    ##### Vehicle Exited #####
    def vehicle_exited(self):
        if self.current_occupancy > 0:
            self.current_occupancy -= 1

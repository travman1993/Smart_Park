
# Main Class
class OccupancyManager:
    ##### Initializing #####
    def __init__(self, max_capacity):
        # Variables
        self.max_capacity = max_capacity
        self.current_occupancy = 0
        self.available_spaces = 0

    ##### Availible Spaces Counter #####
    def get_available_spaces(self):
        self.available_spaces = (self.max_capacity - self.current_occupancy)
        return self.available_spaces

    ##### Full Capacity #####
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

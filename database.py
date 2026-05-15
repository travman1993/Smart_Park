from datetime import datetime

import main

# Main Class
class ParkingDatabase:
    ###### Initializing #####
    def __init__(self):
        # Variables
        self.active_sessions = {}
        self.completed_session = []
        self.residential_plate ={}
        self.vehivle_records = {}
        self.blacklist = []
        self.security_logs = []
        self.total_revenue = 0

    ##### Create Session #####
    def create_session(self, plate, vehicle_type, driver_photo, passenger_photo, mode, entry_time):
        

    ##### Find Active Session #####
    def find_active_session():


    ##### Close Session #####
    def close_session():

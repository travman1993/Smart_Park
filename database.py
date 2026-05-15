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
        session = {
            "plate": plate,
            "vehicle_type": vehicle_type,
            "driver_photo": driver_photo,
            "passenger_photo": passenger_photo,
            "mode": mode,
            "entry_time": entry_time
        }
        self.active_session[plate] = session
        return session

    ##### Find Active Session #####
    def find_active_session(self, plate):
        if plate in self.active_sessions:
            return self.active_sessions[plate]
        else:
            return None

    ##### Close Session #####
    def close_session():
        
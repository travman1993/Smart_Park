from datetime import datetime


# Main Class
class ParkingDatabase:
    ###### Initializing #####
    def __init__(self):
        # Variables
        self.active_sessions = {}
        self.completed_sessions = []
        self.residential_plate ={}
        self.vehicle_records = {}

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
        self.active_sessions[plate] = session
        return session

    ##### Find Active Session #####
    def find_active_session(self, plate):
        if plate in self.active_sessions:
            return self.active_sessions[plate]
        else:
            return None

    ##### Close Session #####
    def close_session(self, plate, exit_time, charge):
        if plate in self.active_sessions:
            session = self.active_sessions[plate]
            session["exit_time"] = exit_time
            session["charge"] = charge
            session["duration"] = (
                exit_time - session["entry_time"]
            )
            self.completed_sessions.append(session)
            del self.active_sessions[plate]
            return session
        return None

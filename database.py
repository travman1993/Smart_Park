from datetime import datetime

class ParkingDatabase:
    def __init__(self):
        self.active_sessions = {}
        self.completed_session = []
        self.residential_plate ={}
        self.vehivle_records = {}
        self.blacklist = []
        self.security_logs = []
        self.total_revenue = 0
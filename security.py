from datetime import datetime

##### Main Class #####
class SecuritySystem:
    def __init__(self):
        self.security_logs = []
        self.blacklisted_plates = {}
        self.tailgate_alerts = []

    ##### Log Denial #####
    def log_denial(self, plate):
        incident = {
            "plate": plate,
            "timestamp": datetime.now(),
            "type": "ACCESS DENIED"
        }
        self.security_logs.append(incident)
        print(f"Security Alert: {plate}")

    ##### Flag Unmatched Exit #####
    def flag_unmatched_exit(self, plate):
        incident = {
            "plate": plate,
            "timestamp": datetime.now(),
            "type": "UNMATCHED EXIT"
        }
        self.security_logs.append(incident)
        print(f"Unmatched Exit Alert: {plate}")

        
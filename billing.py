##### Main Class #####
class BillingEngine:
    ##### Initializing #####
    def __init__(self):
        self.hourly_rate = 5
        self.daily_max = 25
        self.grace_period = 30

    ##### Calculate Charge #####
    def calculate_charge(self, entry_time, exit_time):
        duration = exit_time - entry_time
        minutes_parked = duration.total_seconds() / 60
        charge = 0
        if minutes_parked <= self.grace_period:
            return 0
        
        hours_parked = minutes_parked / 60
        charge = hours_parked * self.hourly_rate 
            
        if charge > self.daily_max:
            charge = self.daily_max
        
        return round(charge, 2)
        
    ##### Process Payment #####
    def process_payment(self, charge):
        # Mock Processing
        print(f"Processing payment: ${charge}")

        return True
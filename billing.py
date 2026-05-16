##### Main Class #####
class BillingEngine:
    ##### Initializing #####
    # Config is passed in so billing never hardcodes its own rates
    def __init__(self, config):
        self.hourly_rate = config.hourly_rate
        self.daily_max = config.daily_max
        self.grace_period = config.grace_period

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
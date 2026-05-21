import time

# UI


# System Modiules
from config import SystemConfig
from database import ParkingDatabase
from sensors import SensorSystem
from security import SecuritySystem
from parking_modes import ModeManager
from gates import GateController
from cameras import CameraSystem
from billing import BillingEngine
from analytics import AnalyticsTracker
from ai_system import AIRecognition 
from occupancy import OccupancyManager
from datetime import datetime

# Main Class - Master controller
class SmartParkSystem:
    ##### Everything is initializing #####
    def __init__(self):
        # Config loads first — all other modules pull their settings from it
        self.config = SystemConfig()

        self.current_mode = self.config.default_mode
        self.running = True
        self.entry_enabled = True
        self.exit_enabled = True

        # Initializing All Modules
        self.database = ParkingDatabase()
        self.sensors = SensorSystem()
        self.camera = CameraSystem()
        self.ai = AIRecognition()
        self.gates = GateController()
        self.billing = BillingEngine(self.config)
        self.occupancy = OccupancyManager(self.config.max_capacity)
        self.analytics  = AnalyticsTracker()
        self.security = SecuritySystem()
        self.parking_modes = ModeManager(self.config.user_selected_mode)

        # System Start UP
        self.start_system()
    
    ##### Start System Funciton #####
    def start_system(self):
        print(f"SYSTEM STARTED — {self.config.facility_name} | Mode: {self.current_mode}")

        self.run()

    ##### Main Loop #####
    def run(self):
        while self.running:
            self.check_entry_sensor()
            self.check_exit_sensor()
            time.sleep(0.1)
    
    def check_entry_sensor(self):
        if self.sensors.entry_triggered():
            self.process_entry()

    def check_exit_sensor(self):
        if self.sensors.exit_triggered():
            self.process_exit()

    ##### Entry Handler #####
    def process_entry(self):
        if self.occupancy.is_full():

            self.gates.keep_closed()

            print("NO ROOM AVAILABLE")

            return
        
        
        # Detect Vehicle Type
        vehicle_type = self.sensors.detect_vehicle_type()
        # Capture Driver, Passenger and Plate Photo
        driver_photo = self.camera.capture_driver()
        passenger_photo = self.camera.capture_passenger()
        plate_photo = self.camera.capture_entry_plate()
        # OCR Plate Check plate for entry
        plate = self.ai.scan_plate(plate_photo)
        # Security Check
        approved = self.ai.validate_access(
            plate,
            self.current_mode
        )
            
        if not approved:
            self.security.log_denial(plate)
            self.gates.keep_closed()
            print("ACCESS DENIED")
            return
            
        entry_time = datetime.now()

        self.database.create_session(
            plate=plate,
            vehicle_type=vehicle_type,
            driver_photo=driver_photo,
            passenger_photo=passenger_photo,
            mode=self.current_mode,
            entry_time=entry_time
        )
        # Update Occupancy
        self.occupancy.vehicle_entered()
        # Update Analytics
        self.analytics.register_vehicle(vehicle_type)
        # Open Gate
        self.gates.open_entry_gate()
        print(f"{plate} entered successfully")
        self.gates.close_gate_after()

    ##### Exit Handler #####
    def process_exit(self):
        # Capture Plate 
        plate_photo = self.camera.capture_exit_plate()
        # AI Scan Plate
        plate = self.ai.scan_plate(plate_photo)
        # Checking Data for active time session
        session = self.database.find_active_session(plate)

        if not session:
            # Sending error and plate scan
            self.security.flag_unmatched_exit(plate)
            print('NO ACTIVE SESSION FOUND')
            return
        
        charge = 0
        payment_success = True
        exit_time = datetime.now()
        duration = exit_time - session["entry_time"]
        print(f"Vehicle stayed: {duration}")

        # Calculating charge based on end of session
        if self.current_mode == "garage":
            # Calculate Charge
            charge = self.billing.calculate_charge(
                session["entry_time"],
                exit_time
            )
            # Payment
            payment_success = self.billing.process_payment(charge)
            # Failed Payment
            if not payment_success:
                print("Payment Failed")
                self.gates.keep_closed()
                return
        # Close Session
        self.database.close_session(
            plate=plate,
            exit_time=exit_time,
            charge=charge
        )
        # Update Occupancy
        self.occupancy.vehicle_exited()
        # Open Gate
        self.gates.open_exit_gate()
        print(f"{plate} exited successfully")
        self.gates.close_gate_after()


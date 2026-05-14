# UI
import tkinter as tk

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

# Main Class - Master controller
class SmartParkSystem:
    # Everything is initializing
    def __init__(self):
        # Variables
        self.current_mode
        self.running
        self.entry_enabled
        self.exit_enabled

        # Initializing All Modules
        self.config = SystemConfig()
        self.database = ParkingDatabase()
        self.sensors = SensorSystem()
        self.camera = CameraSystem()
        self.ai = AIRecognition()
        self.gates = GateController()
        self.billing = BillingEngine()
        self.occupancy = OccupancyManager()
        self.analytics  = AnalyticsTracker()
        self.security = SecuritySystem()
        self.parking_modes = ModeManager()

        # System Start UP
        self.start_system()
    
    # Start System Funciton
    # def start_system(self):

    # Main Loop
    def run(self):
        while self.running:
            check_entry_sensor()
            check_exit_sensor()

    # Entry Handler
    def process_entry(self):
        if self.occupancy.is_full():
            self.gates.keep_closed()
            display_message("NO ROOM AVAILABLE")
        else:
            # Detect Vehicle Type
            vehicle_type = self.sensors.detect_vehicle_type()
            # Capture Driver, Passenger and Plate Photo
            driver_photo = self.camera.capture_driver()
            passenger_photo = self.camera.capture_passenger()
            plate_photo = self.camera.capture_plate()
            # OCR Plate Check plate for entry
            plate = self.ai.scan_plate(plate_photo)
            # Security Check
            approved = self.ai.validate_access(
                plate,
                self.current_mode
            )    

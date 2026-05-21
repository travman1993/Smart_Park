import json
import os

CONFIG_FILE = "park_settings.json"

##### Main Class #####
class SystemConfig:

    ##### Initialize #####
    def __init__(self):
        # These are the default values — used by the wizard as suggestions
        # and as a safety net if a setting is missing from the file
        self.facility_name = ""
        self.max_capacity = 0
        self.default_mode = ""
        self.hourly_rate = 0.0
        self.daily_max = 0.0
        self.grace_period = 0

        if os.path.exists(CONFIG_FILE):
            self._load()
        else:
            self._setup_wizard()
            self._save()

    ##### First-Time Setup Wizard #####
    # Runs only when no config file exists (first launch)
    def _setup_wizard(self):
        print("\n=== Smart Park — First Time Setup ===")

        self.facility_name = input("Facility name: ").strip()
        self.user_selected_mode = input("Choose type of parking mode: ")
        self.default_mode = self.user_selected_mode
        self.max_capacity = self._get_int("Max parking capacity: ")
        self.hourly_rate = self._get_float("Hourly parking rate ($): ")
        self.daily_max = self._get_float("Daily maximum charge ($): ")
        self.grace_period = self._get_int("Grace period before charging (minutes): ")

        print("\nSetup complete. Settings saved to park_settings.json\n")

    ##### Save Settings to File #####
    def _save(self):
        data = {
            "facility_name": self.facility_name,
            "user_selected_mode": self.user_selected_mode,
            "max_capacity": self.max_capacity,
            "default_mode": self.default_mode,
            "hourly_rate": self.hourly_rate,
            "daily_max": self.daily_max,
            "grace_period": self.grace_period,
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

    ##### Load Settings from File #####
    def _load(self):
        with open(CONFIG_FILE, "r") as f:
            data = json.load(f)

        # .get(key, default) safely handles missing keys in older config files
        self.facility_name = data.get("facility_name", "")
        self.user_selected_mode = data.get("user_selected_mode", "")
        self.max_capacity = data.get("max_capacity", 0)
        self.default_mode = data.get("default_mode", "garage")
        self.hourly_rate = data.get("hourly_rate", 0.0)
        self.daily_max = data.get("daily_max", 0.0)
        self.grace_period = data.get("grace_period", 0)

    ##### Update and Re-Save a Setting #####
    # Call this from a settings menu if you add one later
    def update(self, key, value):
        if hasattr(self, key):
            setattr(self, key, value)
            self._save()

    ##### Input Helpers — Retry Until Valid #####
    def _get_int(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("  Please enter a whole number.")

    def _get_float(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("  Please enter a number (e.g. 5.00).")

### Main Class ###
class CameraSystem:
    ### Inizialiting ###
    def __init__(self):
        self.images_captured_entry = []
        self.images_captured_exit = []
        self.activated_camera = False
    
    def capture_driver(self):
        self.activated_camera = True
        log_driver = "driver_photo.jpg"
        print(log_driver)
        self.images_captured_entry.append(log_driver)
        return log_driver

    def capture_passenger(self):
        self.activated_camera = True
        log_passenger = "passenger_photo.jpg"
        print(log_passenger)
        self.images_captured_entry.append(log_passenger)
        return log_passenger

    def capture_entry_plate(self):
        self.activated_camera = True
        log_plate_entry = "plate_img.jpg"
        print(log_plate_entry)
        self.images_captured_entry.append(log_plate_entry)
        return log_plate_entry

    def capture_exit_plate(self):
        self.activated_camera = True
        log_plate_exit = "plate_img.jpg"
        print(log_plate_exit)
        self.images_captured_exit.append(log_plate_exit)
        return log_plate_exit
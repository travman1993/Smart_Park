##### Main Class #####
class AIRecognition:
    ##### Initializing #####
    def __init__(self):
        pass
    
    ##### OCR Plate Check #####
    def scan_plate(self, plate_photo):
        return "ATL4289"

    ##### Validate Access #####
    def validate_access(self, plate, current_mode, residential_plate):
        if current_mode == "residential":
            return plate in residential_plate
        return True
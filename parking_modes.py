##### Main Class #####
class ModeManager:
    ##### Initializing #####
    def __init__(self, mode):
        self.valid_modes = (
            "garage",
            "residential",
            "event",
            "valet"
        )
        self.user_current_mode = mode
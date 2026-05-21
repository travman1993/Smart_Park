### Main Class ###
class GateController:
    ### Initializing ###
    def __init__(self):
        self.closed_gate = True
        self.open_gate = False


    def keep_closed(self):
        self.closed_gate = True
        self.open_gate = False

        print("Gate remains closed")

    def open_entry_gate(self):
        if self.closed_gate is True:

            self.closed_gate = False
            self.open_gate = True

            print("Entry gate opened")

    def open_exit_gate(self):
        if self.closed_gate is True:

            self.closed_gate = False
            self.open_gate = True

            print("Exit gate opened")
    
    def close_gate_after(self):
        
        self.closed_gate = True
        self.open_gate = False

        print("Gate closed back")
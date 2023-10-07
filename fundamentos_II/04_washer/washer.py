from control_panel import ControlPanel
from motor import Motor
from drum import Drum
from water_pump import WaterPump
from dispensers import Dispensers

class WashingMachine:
    def __init__(self):
        self.control_panel = ControlPanel()
        self.motor = Motor()
        self.drum = Drum()
        self.water_pump = WaterPump()
        self.dispensers = Dispensers()

    def start_wash(self, detergent_amount, bleach_amount):
        self.connect_power_source()
        self.motor.rotate_drum()
        self.drum.rinse_clothes()
        self.dispensers.load_detergent(detergent_amount)
        self.dispensers.load_bleach(bleach_amount)

        print("Washing cycle started.")

    def stop_wash(self):
        self.motor.stop_rotation()
        self.disconnect_power_source()
        print("Washing cycle stopped.")

    def load_clothes(self, clothes):
        self.drum.store_clothes(clothes)
        print("Clothes loaded into the drum.")

    def unload_clothes(self):
        unloaded_clothes = self.drum.unload_clothes()
        print("Clothes unloaded from the drum.")
        return unloaded_clothes

    def connect_power_source(self):
        print("Connecting the power source.")
    def disconnect_power_source(self):
        print("Disconnecting the power source.")
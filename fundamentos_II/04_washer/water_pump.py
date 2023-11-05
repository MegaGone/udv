# Clase encargada de manejar las operaciones relacionadas con la bomba de agua.
class WaterPump:
    def __init__(self):
        self.clean_water_level = 0
        self.dirty_water_level = 0

    def load_clean_water(self, amount):
        self.clean_water_level += amount

    def discharge_dirty_water(self, amount):
        if self.dirty_water_level >= amount:
            self.dirty_water_level -= amount
        else:
            print("Error: Insufficient dirty water to discharge.")

    def fill_drum_with_water(self, amount):
        if self.clean_water_level >= amount:
            self.clean_water_level -= amount
            self.dirty_water_level += amount
            print(f"Drum filled with {amount} liters of water.")
        else:
            print("Error: Insufficient clean water to fill the drum.")
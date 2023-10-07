class Drum:
    def __init__(self):
        self.clothes = []

    def rinse_clothes(self):
        if len(self.clothes) > 0:
            print("Rinsing clothes...")
        else:
            print("No clothes in the drum to rinse.")

    def store_clothes(self, new_clothes):
        print("Adding clothes to the drum.")
        self.clothes.extend(new_clothes)

    def unload_clothes(self):
        if len(self.clothes) > 0:
            print("Unloading clothes from the drum.")
            unloaded_clothes = self.clothes[:]
            self.clothes.clear()
            return unloaded_clothes
        else:
            print("The drum is empty. Nothing to unload.")

    def drain_water(self):
        print("Draining water from the drum.")
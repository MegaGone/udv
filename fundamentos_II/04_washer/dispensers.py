# Clase encargada de manejar los dispensadores de detergente y blanqueador.
class Dispensers:
    def __init__(self):
        self.detergent_level = 0
        self.bleach_level = 0

    def load_detergent(self, amount):
        if amount > 0:
            print(f"Loading {amount} grams of detergent.")
            self.detergent_level += amount
        else:
            print("Error: Invalid amount of detergent to load.")

    def load_bleach(self, amount):
        if amount > 0:
            print(f"Loading {amount} milliliters of bleach.")
            self.bleach_level += amount
        else:
            print("Error: Invalid amount of bleach to load.")

    def dispense_detergent(self):
        if self.detergent_level > 0:
            print("Dispensing detergent into the drum.")
            self.detergent_level = 0
        else:
            print("Error: No detergent available to dispense.")

    def dispense_bleach(self):
        if self.bleach_level > 0:
            print("Dispensing bleach into the drum.")
            self.bleach_level = 0
        else:
            print("Error: No bleach available to dispense.")
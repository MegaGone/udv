class Smartphone:
    def __init__(self, brand, model, operating_system):
        self._brand = brand
        self._model = model
        self._operating_system = operating_system
        self._powered_on = False

    def power_on(self):
        if not self._powered_on:
            self._powered_on = True
            print(f"{self._brand} {self._model} has powered on.")
        else:
            print(f"{self._brand} {self._model} is already powered on.")

    def power_off(self):
        if self._powered_on:
            self._powered_on = False
            print(f"{self._brand} {self._model} has powered off.")
        else:
            print(f"{self._brand} {self._model} is already powered off.")

    def make_call(self, number):
        pass

    def send_message(self, contact, message):
        pass
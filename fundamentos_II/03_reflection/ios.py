from smartphone import Smartphone

class iPhone(Smartphone):
    def __init__(self, model):
        super().__init__("Apple", model, "iOS")

    def make_call(self, number):
        if self._powered_on:
            print(f"{self._brand} {self._model} is calling {number}.")
        else:
            print(f"Turn on the {self._brand} {self._model} to make a call.")

    def send_message(self, contact, message):
        if self._powered_on:
            print(f"{self._brand} {self._model} sent a message to {contact}: {message}")
        else:
            print(f"Turn on the {self._brand} {self._model} to send a message.")
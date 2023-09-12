class SmartFridge:
    def __init__(self, brand: str, model: str, water_level: float):
        self.brand = brand
        self.model = model
        self.connected_to_network = False
        self.water_level = water_level

    def connect_to_network(self, network_name: str, password: str) -> None:
        if not self.connected_to_network:
            print(
                f"Connecting fridge {self.brand} {self.model} to {network_name} network...")
            self._perform_connection(network_name, password)
            self.connected_to_network = True
            print("Refrigerator connected to the network.")
        else:
            print("The refrigerator is already connected to the network.")

    def disconnect_from_network(self) -> None:
        if self.connected_to_network:
            print(
                f"Disconnecting fridge {self.brand} {self.model} from the network...")
            self._perform_disconnection()
            self.connected_to_network = False
            print("Fridge disconnected from the network.")
        else:
            print("The fridge is not connected to the network.")

    def dispense_water(self, amount: float) -> None:
        if self.connected_to_network:
            if self._check_water_level(amount):
                print(
                    f"Dispensing {amount} ounces of water from the fridge {self.brand} {self.model}.")
                self._reduce_water_level(amount)
            else:
                print("Not enough water in the fridge to dispense.")
        else:
            print(
                "Cannot dispense water. The fridge is not connected to the network.")

    def _perform_connection(self, network_name: str, password: str) -> None:
        print(
            f"Connecting to the Wi-Fi network {network_name} with the password '{password}'...")

    def _perform_disconnection(self) -> None:
        print("Disconnecting from the Wi-Fi network...")

    def _check_water_level(self, amount: float) -> bool:
        return self.water_level >= amount

    def _reduce_water_level(self, amount: float) -> None:
        self.water_level -= amount
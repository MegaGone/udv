# Clase encargada de manejar los programas de lavado, la temperatura del agua y la duración del ciclo.
class ControlPanel:
    def __init__(self):
        self.wash_programs = []
        self.water_temperature = 0
        self.cycle_duration = 0

    def configure_wash_programs(self, programs):
        self.wash_programs = programs

    def set_water_temperature(self, temperature):
        if 0 <= temperature <= 100:
            self.water_temperature = temperature
        else:
            print("Error: Invalid water temperature setting. Please choose a value between 0°C and 100°C.")

    def set_cycle_duration(self, duration):
        if duration > 0:
            self.cycle_duration = duration
        else:
            print("Error: Invalid cycle duration. Please choose a positive duration in minutes.")
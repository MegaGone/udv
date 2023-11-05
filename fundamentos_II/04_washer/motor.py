# Clase encargada de manejar las funcionalidades relacionadas con el motor.
class Motor:
    def __init__(self):
        self.speed = 0
        self.is_rotating = False

    # Métodos rotate_drum y stop_rotation de la clase original Motor
    def rotate_drum(self):
        if not self.is_rotating:
            print("Starting drum rotation.")
            self.speed = 100
            self.is_rotating = True
        else:
            print("The drum is already rotating.")

    def stop_rotation(self):
        if self.is_rotating:
            print("Stopping drum rotation.")
            self.speed = 0 
            self.is_rotating = False
        else:
            print("The drum is already stopped.")
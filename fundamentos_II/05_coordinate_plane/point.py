class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    
    # DETERMINAR EL CUADRANTE EN DONDE SE ENCUENTRA EL PUNTO
    def quadrant(self):
        if self.x[0] == '-' and self.y[0] != '-':
            print(f'El punto {self} esta en el cuadrante 2')
        elif self.x[0] == '-' and self.y[0] == '-':
            print(f'El punto {self} esta en el cuadrante 3')
        elif self.y[0] == '-':
            print(f'El punto {self} esta en el cuadrante 4')
        else:
            print(f'El punto {self} esta en el cuadrante 1')
        return [int(self.x), int(self.y)]
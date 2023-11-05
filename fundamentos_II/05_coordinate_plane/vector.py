from point import Point

class Vector(Point):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    # CALCULA EL VECTOR ENTRE DOS PUNTOS
    def calculate_vector(self, p1, p2):
        result_x = p2[0] - p1[0]
        result_y = p2[1] - p1[1]
        print(f'Resultado de X: {result_x}')
        print(f'Resultado de Y: {result_y}')
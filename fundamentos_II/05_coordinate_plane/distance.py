from point import Point
import math

class Distance(Point):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)

    # CALCULA LA DISTANCIA ENTRE LOS DOS PUNTOS USANDO LA LIBRERÍA MATH
    def calculate_distance(self, p1, p2):
        distance = math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)
        return distance
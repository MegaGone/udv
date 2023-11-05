from point import Point
from vector import Vector
from distance import Distance
from validations import input_coordinate

if __name__ == '__main__':
    # Solicitar al usuario los dos puntos
    x1 = input_coordinate("Ingrese la coordenada x del primer punto (debe ser un solo dígito): ")
    y1 = input_coordinate("Ingrese la coordenada y del primer punto (debe ser un solo dígito): ")
    x2 = input_coordinate("Ingrese la coordenada x del segundo punto (debe ser un solo dígito): ")
    y2 = input_coordinate("Ingrese la coordenada y del segundo punto (debe ser un solo dígito): ")

    # Crear los puntos con las coordenadas ingresadas
    point1 = Point(x1, y1)
    point2 = Point(x2, y2)

    # Calcular el cuadrante de cada punto
    point1_quadrant = point1.quadrant()
    point2_quadrant = point2.quadrant()

    # Calcular el vector resultante
    vector = Vector()
    vector.calculate_vector(point1_quadrant, point2_quadrant)

    # Calcular la distancia entre los dos puntos
    distance = Distance()
    calculated_distance = distance.calculate_distance(point1_quadrant, point2_quadrant)
    print(f"La distancia entre los dos puntos es: {calculated_distance}")

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/05_coordinate_plane/
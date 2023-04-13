# INICIO CALCULAR_LONGITUD_RECTA
# importar libreria math
# declarar float_x1 = 0, float_y1 = 0, float_x2 = 0, float_y2 = 0, float_length = 0
#
# Repetir mientras float_x1 && float_y1 no sea un número válido
#   Imprimir Ingrese la coordenada x del primer punto:
#   leer float_x1
#   Imprimir Ingrese la coordenada y del primer punto:
#   leer float_y1
#   salir del ciclo
# Excepto CoordenadasNoValidas
#   Imprimir Las coordenadas del primer punto no son válidas. Intente nuevamente.
#
# Repetir mientras float_x2 && float_y2 no sea un número válido
#   Imprimir Ingrese la coordenada x del segundo punto:
#   leer float_x2
#   Imprimir Ingrese la coordenada y del segundo punto:
#   leer float_y2
#   salir del ciclo
# Excepto CoordenadasNoValidas
#   Imprimir Las coordenadas del segundo punto no son válidas. Intente nuevamente.
#
# Procesar float_length = raíz_cuadrada_de((float_x2 - float_x1) al_cuadrado + (float_y2 - float_y1) al_cuadrado)
#
# Imprimir La longitud de la recta es:
# Mostrar float_length
# FIN CALCULAR_LONGITUD_RECTA
#

import math

float_x1 = 0
float_y1 = 0
float_x2 = 0
float_y2 = 0
float_length = 0

while True:
    try:
        float_x1 = float(input("Ingrese la coordenada x del primer punto: "))
        float_y1 = float(input("Ingrese la coordenada y del primer punto: "))
        break
    except ValueError:
        print("Las coordenadas del primer punto no son válidas. Intente nuevamente.")

while True:
    try:
        float_x2 = float(input("Ingrese la coordenada x del segundo punto: "))
        float_y2 = float(input("Ingrese la coordenada y del segundo punto: "))
        break
    except ValueError:
        print("Las coordenadas del segundo punto no son válidas. Intente nuevamente.")

# PROCESOS
float_length = math.sqrt((float_x2 - float_x1)**2 + (float_y2 - float_y1)**2)

print(f"La longitud de la recta es: {float_length}")
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/14_length_line.py
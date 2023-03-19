# INICIO CALCULAR_ÁREA
# declarar float_base = 0, float_height = 0, float_area = 0
#
# Repetir mientras float_base no sea un numero válido
#   imprimir "Ingrese la base del triángulo: "
#   leer float_base
#   salir del ciclo
# excepto BaseNoVálida:
#   imprimir "La base debe ser un número positivo. Intente nuevamente."
#
# Repetir mientras float_height no sea un numero válido
#   imprimir "Ingrese la altura del triángulo: "
#   leer float_height
#   salir del ciclo
# excepto HeightNoVálida:
#   imprimir "La altura debe ser un número positivo. Intente nuevamente."
#
# procesar float_area = float_base * float_height / 2
#
# imprimir "El área del triángulo es: float_area"
# impirmir "Presione enter para cerrar el programa..."
#
# FIN CALCULAR_ÁREA

# VARIABLES
float_base = 0
float_height = 0
float_area = 0

while True:
    try:
        float_base = float(input("Ingrese la base del triángulo: "))
        break
    except ValueError:
        print("La base debe ser un número positivo. Intente nuevamente.")

while True:
    try:
        float_height = float(input("Ingrese la altura del triángulo: "))
        break
    except ValueError:
        print("La altura debe ser un número positivo. Intente nuevamente.")

float_area = float_base * float_height / 2

print(f"El área del triángulo es: {float_area}")
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/07_training_III.py
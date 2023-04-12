# INICIO CALCULAR_VOLUMEN_CILINDRO
# declarar float_pi = 3.1416, float_diameter = 0, float_height = 0, float_radius = 0, float_area = 0, float_volume = 0
#
# Repetir mientras float_diameter no sea un número válido
#   Imprimir Ingrese el diametro del cilindro:
#   leer float_diameter
#   salir del ciclo
# Excepto DiametroNoVálido
#   Imprimir El diametro debe ser un número positivo. Intente nuevamente.
#
# Repetir mientras float_height no sea un número válido
#   Imprimir Ingrese la altura del cilindro:
#   leer float_height
#   salir del ciclo
# Excepto AlturaNoVálida
#   Imprimir La altura debe ser un número positivo. Intente nuevamente.
#
# Procesar float_radius = float_diameter divido 2
# Procesar float_area = float_pi
# float_volume = float_area * float_height
#
# Imprimir El volumen del cilindro es
# Mostrar float_volume
# 
# FIN CALCULAR_VOLUMEN_CILINDRO

# CONSTANTES
float_pi = 3.1416

# VARIABLES
float_diameter = 0
float_height = 0
float_radius = 0
float_area = 0
float_volume = 0

# ENTRADAS
while True:
    try:
        float_diameter = float(input("Ingrese el diametro del cilindro: "))
        break
    except ValueError:
        print("El diametro debe ser un número positivo. Intente nuevamente.")

while True:
    try:
        float_height = float(input("Ingrese la altura del cilindro: "))
        break
    except ValueError:
        print("La altura debe ser un número positivo. Intente nuevamente.")

# PROCESOS
float_radius = float_diameter / 2
float_area = float_pi * float_radius**2
float_volume = float_area * float_height

# SALIDAS
print(f"El volumen del cilindro es {float_volume}")
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/13_cylinder.py
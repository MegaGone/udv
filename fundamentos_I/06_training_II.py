# INICIO CONVERTIR_CELCIUS_A_FAHRENHEIT
# declarar fahrenheit_degrees = 0, celsius_degrees = 0
#
# Repetir mientras celsius_degrees no sea un numero válido
#   Imprimir "Ingrese un número: "
#   Leer celsius_degrees
#   salir del ciclo
#
# excpeto CelciusNoVálidos:
# imprimir "Temperatura no válida. Intente nuevamente."
#
# PROCESAR fahrenheit_degrees = celsius_degrees * 1.8 + 32 
#
# Imprimir "celsius_degrees grados Celsius equivale a fahrenheit_degrees grados Fahrenheit."
# Imprimir "Presione enter para cerrar..."
#
# FIN CONVERTIR_CELCIUS_A_FAHRENHEIT

fahrenheit_degrees = 0
celsius_degrees = 0

while True:
    try:
        celsius_degrees = float(input("Ingrese un número: "))
        break
    except ValueError:
        print("Temperatura no válida. Intente nuevamente.")

fahrenheit_degrees = celsius_degrees * 1.8 + 32

print(f"{celsius_degrees} grados Celsius equivale a {fahrenheit_degrees} grados Fahrenheit.")
input("Presione enter para cerrar...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/06_training_II.py
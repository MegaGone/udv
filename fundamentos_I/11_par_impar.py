# INICIO NÚMERO_PAR_O_IMPAR
#
# declarar int_numero = 0
# 
# repetir mientras int_numero no sea un número válido
#   imprimir Ingrese un número entero: 
#   leer int_numero
#   parar ciclo
# Excepto número no válido:
#  imprimir Número no válido. Ingrese otro número
#
# Si el residuo de int_numero es exactamente igual a 0
#   mostrar El número es par.
# De lo contrario
#   mostrar El número es impar.
# 
# FIN NÚMERO_PAR_O_IMPAR

int_numero = 0

while True:
    try:
        int_numero = int(input("Ingrese un número entero: "))
        break
    except ValueError:
        print("Número no válido. Ingrese otro número")

if int_numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

input("\nPresione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/11_par_impar.py
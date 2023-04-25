# INICIO DIVISORES_N_NUMERO
# declarar int_dividend = 0, arr_int_divisors = []
#
# Repetir mientras int_dividend no sea un numero
# Intentar
#
#   Imprimir Ingresa un número entero positivo: 
#   leer int_dividend
#   Si int_dividend es menor o igual a 0
#       Imprimir El número debe ser mayor que cero.
#   salir del ciclo
#
# Para cada int_index desde 1 hasta int_dividend:
#   Si int_dividend divido int_index es igual a 0, entonces:
#       Añadir a arr_int_divisors int_index
#
# Convertir todos los elementos de arr_int_divisors a una cadena de texto.
# Unir los elementos de la cadena con ', ' como separador.
# Almacenar la cadena resultante en la variable "arr_int_divisors".
#
# Imprimir Los divisores de int_dividend son
# Imprimir arr_int_divisors
#
# FIN DIVISORES_N_NUMERO

int_dividend = 0
arr_int_divisors = []

# ENTRADAS
while True:
    try:
        int_dividend = int(input("Ingresa un número entero positivo: "))
        if int_dividend <= 0:
            raise ValueError("El número debe ser mayor que cero.")
        break
    except ValueError:
        print("El dividendo no es válido. Ingrese uno diferente.")

# PROCESOS
for i in range(1, int_dividend):
    if int_dividend % i == 0:
        arr_int_divisors.append(i)

arr_int_divisors = ', '.join(map(str, arr_int_divisors))

# SALIDAS
print("Los divisores de", int_dividend, "son:", arr_int_divisors)
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/16_divisors.py
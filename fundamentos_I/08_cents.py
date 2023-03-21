# INICIO CALCULAR_CENTAVOS
# 
# intmonedas_50 = 0, intmonedas_25 = 0, intmonedas_10 = 0, intmonedas_5 = 0, intmonedas_1 = 0, centavos_totales = 0
# 
# Repetir mientras centavos_totales no sea válido:
# intentar:
#   imprimir "Ingrese la cantidad total de centavos: "
#   leer centavos_totales
#   salir del ciclo
#
# si centavos_totales <= 0 o centavos_totales > 100:
#   imprimir "La cantidad debe ser mayor que 0 y menor o igual que 100"
# 
# excepto CentavosNoVálidos:
#   imprimir "Ingrese una cantidad de centavos válidos"
#
# intmonedas_50 = centavos_totales // 50
# intmonedas_50 = centavos_totales // 50
# centavos_totales = centavos_totales % 50
#
# intmonedas_25 = centavos_totales // 25
# centavos_totales = centavos_totales % 25
#
# intmonedas_10 = centavos_totales // 10
# centavos_totales = centavos_totales % 10
#
# intmonedas_5 = centavos_totales // 5
# centavos_totales = centavos_totales % 5
#
# intmonedas_1 = centavos_totales
#
# imprimir intmonedas_50
# imprimir "moneda de 50"
#
# imprimir intmonedas_25
# imprimir "moneda de 25"
#
# imprimir intmonedas_10
# imprimir "moneda de 10"
#
# imprimir intmonedas_5
# imprimir "moneda de 5"
#
# imprimir intmonedas_1
# imprimir "moneda de 1"
#
# FIN CALCULAR_CENTAVOS

# VARIABLES
intmonedas_50 = 0
intmonedas_25 = 0
intmonedas_10 = 0
intmonedas_5 = 0
intmonedas_1 = 0
centavos_totales = 0

while True:
    try:
        centavos_totales = int(input("Ingrese la cantidad de centavos no mayor a 100: "))
        if centavos_totales < 1 or centavos_totales > 100:
            print("La cantidad de centavos debe ser mayor a 0 y menor o igual a 100")
        else:
            break
    except ValueError:
        print("Centavos no válidos. Intente de nuevo")

intmonedas_50 = centavos_totales // 50
centavos_totales = centavos_totales % 50

intmonedas_25 = centavos_totales // 25
centavos_totales = centavos_totales % 25

intmonedas_10 = centavos_totales // 10
centavos_totales = centavos_totales % 10

intmonedas_5 = centavos_totales // 5
centavos_totales = centavos_totales % 5

intmonedas_1 = centavos_totales

print(f"\n{intmonedas_50} moneda de 50")
print(f"{intmonedas_25} moneda de 25")
print(f"{intmonedas_10} moneda de 10")
print(f"{intmonedas_5} moneda de 5")
print(f"{intmonedas_1} moneda de 1")

input("\nPresione enter para cerrar...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/08_cents.py
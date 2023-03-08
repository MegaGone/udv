# INICIO CALCULAR_FECHAS
# declarar int_days, int_months, int_years, int_maxdaysbyyear = 365, int_maxdaysbymonth = 30
#
# Repetir mientras int_days no sea un numero válido
#
# intentar:
#   Imprimir "Ingrese la cantidad de días que desea convertir: "
#   Leer int_days
#   salir del ciclo
#
# excepto DíasNoVálidos:
# Imprimir "Días no válidos. Intente de nuevo"
#
# int_years = int(int_days / int_maxdaysbyyear)
# int_days -= int_years * int_maxdaysbyyear
# int_months = int(int_days / int_maxdaysbymonth)
# int_days -= int_months * int_maxdaysbymonth
#
# Imprimir "Años calculados: "
# Mostrar int_years
# Imprimir "Meses calculados: "
# Mostrar int_months
# Imprimir "Días calculados: "
# Mostrar int_days
#
# FIN CALCULAR_FECHAS

# CONSTANTES
int_maxdaysbyyear = 365
int_maxdaysbymonth = 30

# VARIABLES
int_days = 0
int_months = 0
int_years = 0

while True:
    try:
        int_days = int(input("Ingrese el número de días: "))
        break
    except ValueError:
        print("Días no válidos. Intente de nuevo")

int_years = int(int_days / int_maxdaysbyyear)
int_days -= int_years * int_maxdaysbyyear
int_months = int(int_days / int_maxdaysbymonth)
int_days -= int_months * int_maxdaysbymonth

print(f"\nLos días convertidos són: {int_years} años, {int_months} meses y {int_days} días")
input('Presione enter para cerrar el programa...')

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/04_quiz_I.py
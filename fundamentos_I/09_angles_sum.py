# INICIO SUMA_DE_DOS_ÁNGULOS
#
# int_angle1 = 0, int_angle2 = 0, int_grades1 = 0, int_minutes1 = 0, int_seconds1 = 0, int_grades2 = 0, int_minutes2 = 0, int_seconds2 = 0
# int_sumgrades = 0, int_summinutes = 0, int_sumseconds = 0
#
# Imprimir "Ingrese el primer ángulo en formato grados minutos segundos: "
# Leer int_angle1
#
# Si la longitud de "int_angle1" por espacios en blanco no es igual a 3 o alguno de los elementos en la lista no es un número o es un número negativo, entonces:
#   Imprimir "[ERROR] El formato del primer ángulo no es válido."
#   Salir del programa
#
# Imprimir "Ingrese el segundo ángulo en formato grados minutos segundos: "
# Leer int_angle1
#
# Si la longitud de "int_angle2" por espacios en blanco no es igual a 3 o alguno de los elementos en la lista no es un número o es un número negativo, entonces:
#   Imprimir "[ERROR] El formato del segundo ángulo no es válido."
#   Salir del programa
#
# Asignar int_grades1, int_minutes1, int_seconds1 los valores enteros resultantes de la función map a int_angle1 al dividirlo por espacios en blanco
# Asignar int_grades2, int_minutes2, int_seconds2 los valores enteros resultantes de la función map a int_angle2 al dividirlo por espacios en blanco
#
# int_sumgrades = int_grades1 + int_grades2
# int_summinutes = int_minutes1 + int_minutes2
# int_sumseconds = int_seconds1 + int_seconds2
#
# Si int_sumseconds >= 60:
#   int_summinutes += 1
#   int_sumseconds -= 60
#
# Si int_summinutes >= 60:
#   int_sumgrades += 1
#   int_summinutes -= 60
#
# Imprimir La suma de los grados es:
# Imprimir int_sumgrades
#
# Imprimir La suma de los minutos es:
# Imprimir int_summinutes
#
# Imprimir La suma de los segundos es:
# Imprimir int_sumseconds
#
# FIN SUMA_DE_DOS_ÁNGULOS

# VARIABLES
int_angle1 = 0
int_angle2 = 0
int_grades1 = 0
int_minutes1 = 0
int_seconds1 = 0
int_grades2 = 0
int_minutes2 = 0
int_seconds2 = 0
int_sumgrades = 0
int_summinutes = 0
int_sumseconds = 0

# VALIDACIONES O RESTRICCIONES DE LAS ENTRADAS
int_angle1 = input("Ingrese el primer ángulo en formato grados minutos segundos: ")
if len(int_angle1.split()) != 3 or not all(x.isdigit() and int(x) >= 0 for x in int_angle1.split()):
    print("[ERROR] El formato del primer ángulo no es válido.")
    exit()

int_angle2 = input("Ingrese el segundo ángulo en formato grados minutos segundos: ")
if len(int_angle2.split()) != 3 or not all(x.isdigit() and int(x) >= 0 for x in int_angle2.split()):
    print("[ERROR] El formato del segundo ángulo no es válido.")
    exit()

# PROCESOS
int_grades1, int_minutes1, int_seconds1 = map(int, int_angle1.split())
int_grades2, int_minutes2, int_seconds2 = map(int, int_angle2.split())

int_sumgrades = int_grades1 + int_grades2
int_summinutes = int_minutes1 + int_minutes2
int_sumseconds = int_seconds1 + int_seconds2

if int_sumseconds >= 60:
    int_summinutes += 1
    int_sumseconds -= 60
if int_summinutes >= 60:
    int_sumgrades += 1
    int_summinutes -= 60

# SALIDA
print(f"\nLa suma de los grados es: {int_sumgrades}")
print(f"La suma de los minutos es: {int_summinutes}")
print(f"La suma de los segundos es: {int_sumseconds}")

input("\nPresione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/09_angles_sum.py
# INICIO DEL PROGRAMA
# username, width, height 
#
# Imprimir "Ingrese su nombre: "
# Leer username
# Mientras no username hacer
#     Imprimir "Valor incorrecto. Ingrese un nombre correcto y sin espacios: "
#     Leer username
# Fin mientras
#
# Imprimir "Ingrese la anchura: "
# Leer width
# Imprimir "Ingrese la altura: "
# Leer height
#
# Mientras no (es_entero(width) and es_entero(height) and int(width) > 0 and int(height) > 0) hacer
#     Si no es_entero(width) o int(width) <= 0 entonces
#         Imprimir "Anchura incorrecta. Ingrese una anchura válida y mayor a 0: "
#         Leer width
#     Sino si no es_entero(height) o int(height) <= 0 entonces
#         Imprimir "Altura incorrecta. Ingrese una altura válida y mayor a 0: "
#         Leer height
#     Fin si
# Fin mientras

# Imprimir "Estimado " + username + ", sus resultados son los siguientes:"
# Imprimir "El Primer resultado es de tipo float: ", int(width) / 2
# Imprimir "El Segundo resultado es de tipo float: ", int(width) / 2.0
# Imprimir "El Tercer resultado es de tipo float: ", int(height) / 3
# Imprimir "El Cuarto resultado es de tipo int: ", 1 + 2 * 5
# FIN DEL PROGRAMA

username = ''
width = 0
height = 0

username = input('Ingrese su nombre: ').strip()

while not username:
    username = input('Valor incorrecto. Ingrese un nombre correcto y sin espacios: ').strip()

width = input('Ingrese la anchura: ')
height = input('Ingrese la altura: ')

while not width.isdigit() or int(width) <= 0 or not height.isdigit() or int(height) <= 0:
    if not width.isdigit() or int(width) <= 0:
        width = input('Anchura incorrecta. Ingrese una anchura válida y mayor a 0: ')
    elif not height.isdigit() or int(height) <= 0:
        height = input('Altura incorrecta. Ingrese una altura válida y mayor a 0: ')

print(f'\nEstimado {username} sus resultados son los siguientes:')
print(f'El Primer resultado es de tipo { type(int(width)/2).__name__ }: ',  int(width)/2)
print(f'El Segundo resultado es de tipo { type(int(width)/2.0).__name__ }: ', int(width)/2.0)
print(f'El Tercer resultado es de tipo { type(int(height)/3).__name__ }: ',  int(height)/3)
print(f'El Cuarto resultado es de tipo { type(1 + 2 * 5).__name__ }: ', 1 + 2 * 5)
print('\nHecho por Jimmy Martinez - Carné No. 202302745')
input("Presione enter para salir...")

## Jimmy Martinez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/exerciseI.py
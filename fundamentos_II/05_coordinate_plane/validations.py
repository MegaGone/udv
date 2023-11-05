import re

def validate_coordinate(coordinate):
    # Patrón que acepta un número positivo o negativo de 1 a 4 dígitos, o un dígito opcionalmente seguido por otro dígito
    pattern = re.compile(r'^-?\d{1,4}$|^-?\d\d?$')
    return bool(re.match(pattern, coordinate))

def input_coordinate(message):
    while True:
        coordenada = input(message)
        if validate_coordinate(coordenada):
            return coordenada
        else:
            print("Formato incorrecto. Debe ser un número posítivo o negativo. Intente de nuevo.")
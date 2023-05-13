import pwinput

def mostrar_menu():
    print("******************* AHORCADO UDV *******************")
    print("1. Iniciar nueva partida")
    print("2. Salir del juego")

    try:
        int_option = int(input("Seleccione una opción: "))
        if int_option > 0 and int_option < 3:
            return int_option
        else:
            print("[ERROR] La opción seleccionada no es válida.\n")
    except ValueError:
        print("[ERROR] La opción debe ser un número entero positivo.\n")

def obtener_palabra():
    while True:
        str_palabra = pwinput.pwinput(prompt='\nIngrese la palabra a adivinar: ')
        palabras = str_palabra.split()

        if all(palabra.isalpha() for palabra in palabras) and all(len(palabra) > 1 for palabra in str_palabra.split(" ")):
            return str_palabra.lower()
        else:
            print("[ERROR] La palabra solo puede contener letras y los espacios no deben ser más de 1 seguido.")

def obtener_categoria():
    while True:
        str_categoria = input("Ingrese la categoría a la cuál pertenece la palabra: ")
        if str_categoria.isalpha():
            return str_categoria
        else:
            print("[ERROR] La categoría solo puede contener letras.")

def mostrar_guiones(palabra):
    guiones = "\n"
    for letra in palabra:
        guiones += "_ "
    return guiones

def mostrar_detalles(str_palabra, str_categoria, int_intentos):
    print(f"\nLetras: { len(str_palabra) }")
    print(f"Categoría: { str_categoria }")
    print(f"Intentos disponibles: { int_intentos }\n")

def validar_letra(str_letra, str_palabra):
    # if len(str_letra) > 1 or not str_letra.isalpha():
    if len(str_letra) > 1:
        return False
    else:
        str_letra = str_letra.lower()
        if str_letra in str_palabra:
            return True

def comparar_letras(letra, palabra, palabra_oculta):
    nueva_palabra_oculta = ""
    for i in range(len(palabra)):
        if palabra[i] == letra:
            nueva_palabra_oculta += letra + " "
        else:
            nueva_palabra_oculta += palabra_oculta[i*2:i*2+2]
    return nueva_palabra_oculta.strip()

def validar_palabras(str_palabra_oculta, str_palabra):
    str_palabra_oculta = ''.join(str_palabra_oculta.split())
    str_palabra = ''.join(str_palabra.split())

    if str_palabra_oculta == str_palabra:
        return True
    else:
        return False
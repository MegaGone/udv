import pwinput
import re
import os

def mostrar_menu():
    print("******************* AHORCADO UDV *******************")
    print("1. INICIAR UNA NUEVA PARTIDA")
    print("2. SALIR DEL JUEGO")
    print("3. LIMPIAR CONSOLA")
    print("****************************************************")

    try:
        int_option = int(input("SELECCIONE UNA OPCIÓN: "))
        if int_option > 0 and int_option < 4:
            return int_option
        else:
            print("[ERROR] LA OPCIÓN SELECCIONADA NO ES VÁLIDA.\n")
    except ValueError:
        print("[ERROR] LA OPCIÓN DEBE SER UN NÚMERO ENTERO POSITIVO.\n")

def obtener_palabra():
    while True:
        str_palabra = pwinput.pwinput(prompt='\nINGRESE LA PALABRA A ADIVINAR: ')

        if re.match("^[a-zA-Z]+$", str_palabra):
            return str_palabra.lower()
        else:
            print("[ERROR] LA PALABRA SOLO PUEDE CONTENER LETRAS.")

def obtener_categoria():
    while True:
        str_categoria = input("INGRESE LA CATEGORÍA A LA CUÁL PERTENECE LA PALABRA: ")
        if str_categoria.isalpha():
            return str_categoria
        else:
            print("[ERROR] LA CATEGORÍA SOLO PUEDE CONTENER LETRAS.")

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
    if len(str_letra) > 1 or not str_letra.isalpha():
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
    
def limpiar_consola():
    os.system('cls')

def mostrar_figura(intentos):
    figura = [
        """
          ____
         |    |
         |    
         |    
         |    
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |    
         |    
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |    |
         |    
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |   /|
         |    
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |   /|\\
         |    
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |   /|\\
         |   / 
         |    
        _|_
        """,
        """
          ____
         |    |
         |    O
         |   /|\\
         |   / \\
         |    
        _|_
        """
    ]
    print(figura[::-1][intentos])
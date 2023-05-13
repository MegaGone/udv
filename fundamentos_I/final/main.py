import sys
from helpers.functions import obtener_palabra, obtener_categoria, mostrar_guiones, mostrar_detalles, mostrar_menu, validar_letra

# while True:
int_opcion = mostrar_menu()
int_intentos = 6
str_letra = ""

if int_opcion == 1:    
    str_palabra = obtener_palabra()
    str_categoria = obtener_categoria()
    str_palabra_oculta = mostrar_guiones(str_palabra)
    print(str_palabra_oculta)
    mostrar_detalles(str_palabra, str_categoria, int_intentos)
    # pass

    while True:
        if int_intentos > 0:
            str_letra = input("Ingrese una letra: ")
            bool_letra_en_palabra = validar_letra(str_letra, str_palabra)

            if bool_letra_en_palabra != True:
                int_intentos -= 1
                mostrar_detalles(str_palabra, str_categoria, int_intentos)
            else:
                # TODO: Replace letter in str_palabra_oculta
                print(str_palabra_oculta)

        else:
            print("Juego terminado")
            break

elif int_opcion == 2:
    print("bye")
    sys.exit()
import sys
from helpers.functions import obtener_palabra, obtener_categoria, mostrar_guiones, mostrar_detalles, mostrar_menu, validar_letra, comparar_letras, validar_palabras, limpiar_consola

while True:
    int_opcion = mostrar_menu()
    int_intentos = 6
    str_letra = ""

    if int_opcion == 1:    
        str_palabra = obtener_palabra()
        str_categoria = obtener_categoria()
        str_palabra_oculta = mostrar_guiones(str_palabra)
        print(str_palabra_oculta)
        mostrar_detalles(str_palabra, str_categoria, int_intentos)

        while True:
            if int_intentos > 0:
                str_letra = input("Ingrese una letra: ")
                bool_letra_en_palabra = validar_letra(str_letra, str_palabra)

                if bool_letra_en_palabra != True:
                    int_intentos -= 1
                    mostrar_detalles(str_palabra, str_categoria, int_intentos)
                else:
                    str_palabra_oculta = comparar_letras(str_letra, str_palabra, str_palabra_oculta)
                    print(str_palabra_oculta)
                    bool_palabra_adivinada = validar_palabras(str_palabra_oculta, str_palabra)
                    mostrar_detalles(str_palabra, str_categoria, int_intentos)

                    if bool_palabra_adivinada == True:
                        print("Felicidades, ha adivinado la palabra")
                        break
            else:
                print(f"Ooops! Se ha quedado sin intentos, la palabra correcta era: { str_palabra }")
                break

    elif int_opcion == 2:
        print("Gracias por jugar!")
        input("Presione enter para cerrar el programa...")
        sys.exit()

    elif int_opcion == 3:
        limpiar_consola()
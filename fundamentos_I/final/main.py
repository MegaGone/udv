import sys
from helpers.functions import (
    obtener_palabra, 
    obtener_categoria, 
    mostrar_guiones, 
    mostrar_detalles, 
    mostrar_menu, 
    validar_letra, 
    comparar_letras, 
    validar_palabras, 
    limpiar_consola, 
    mostrar_figura, 
    obtener_jugador,
    crear_registro,
    cargar_historial
)

while True:
    int_opcion = mostrar_menu()
    int_intentos = 6
    str_letra = ""
    bool_palabra_adivinada = False

    if int_opcion == 1:    
        str_palabra = obtener_palabra()
        str_categoria = obtener_categoria()
        str_nombre_jugador = obtener_jugador()
        str_palabra_oculta = mostrar_guiones(str_palabra)
        print(str_palabra_oculta)
        mostrar_detalles(str_palabra, str_categoria, int_intentos)

        while True:
            if int_intentos > 0:
                str_letra = input("INGRESE UNA LETRA: ")
                bool_letra_en_palabra = validar_letra(str_letra, str_palabra)

                if bool_letra_en_palabra != True:
                    int_intentos -= 1
                    mostrar_figura(int_intentos)
                    mostrar_detalles(str_palabra, str_categoria, int_intentos)
                else:
                    str_palabra_oculta = comparar_letras(str_letra, str_palabra, str_palabra_oculta)
                    print(str_palabra_oculta)
                    bool_palabra_adivinada = validar_palabras(str_palabra_oculta, str_palabra)
                    mostrar_detalles(str_palabra, str_categoria, int_intentos)

                    if bool_palabra_adivinada == True:
                        print("FELICIDADES, HA ADIVINADO LA PALABRA")
                        crear_registro(str_nombre_jugador, str_palabra, str_categoria , bool_palabra_adivinada)
                        break
            else:
                print("JUEGO TERMINADO.")
                print(f"LA PALABRA CORRECTA ERA: { str_palabra }")
                crear_registro(str_nombre_jugador, str_palabra, str_categoria, bool_palabra_adivinada)
                break

    elif int_opcion == 2:
        limpiar_consola()
        print("GRACIAS POR JUGAR!")
        print("JIMMY MARTINEZ - 202302745")
        input("PRESIONE ENTER PARA CERRAR EL PROGRAMA...")
        sys.exit()

    elif int_opcion == 3:
        limpiar_consola()

    elif int_opcion == 4:
        arr_historial = cargar_historial()
        print(arr_historial)
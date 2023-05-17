import time
import os
import pwinput

def piedra_papel_tijera():
    os.system('cls')
    arr_opciones = ["piedra", "papel", "tijera"]
    str_jugador1 = pwinput.pwinput(prompt='[JUGADOR 1] Elige piedra, papel o tijera: ')
    str_jugador2 = pwinput.pwinput(prompt='[JUGADOR 2] Elige piedra, papel o tijera: ')

    if str_jugador1.lower() not in arr_opciones or str_jugador2.lower() not in arr_opciones:
        print("[ERROR] Opción no válida, elige otra opción.")
        return

    os.system('cls')
    print("PIEDRA, PAPEL O TIJERA...")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    str_jugador1 = str_jugador1.lower()
    str_jugador2 = str_jugador2.lower()

    if str_jugador1 == str_jugador2:
        print("Empate. Ambos jugadores eligieron", str_jugador1)
    elif (str_jugador1 == "piedra" and str_jugador2 == "tijera") or (str_jugador1 == "papel" and str_jugador2 == "piedra") or (str_jugador1 == "tijera" and str_jugador2 == "papel"):
        print("[JUGADOR 1] Ganador. ", str_jugador1, "vence a", str_jugador2)
    else:
        print("[JUGADOR 2] Ganador. ", str_jugador2, "vence a", str_jugador1)

    print("\nJIMMY MARTÍNEZ - CARNET NO. 202302745")
    input("Presione enter para cerrar el programa...")

piedra_papel_tijera()

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/19_rock_paper_scissors.py
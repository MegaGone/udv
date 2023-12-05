from pila import Pila

pila = Pila()

# SOLICITAR LOS ELEMENTOS
for i in range(5):
    while True:
        try:
            # APILAMOS SI ES UN ENTERO VÁLIDO
            elemento = int(input(f"Ingrese el a apilar: "))
            pila.apilar(elemento)

            # DESAPILAMOS CUANDO LOS ELEMENTOS SEAN MAYOR A 3
            if len(pila.elementos) > 3:
                pila.desapilar()
            break
        except ValueError:
            print("[ERROR] Solamente están permitidos los valores enteros.")

print("Elementos restantes en la pila:", pila.elementos)
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/08_final/
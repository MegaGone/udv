from pila import Pila
from validation import NoPositiveNumberException

pila = Pila()

# SOLICITAR LOS ELEMENTOS
for i in range(5):
    while True:
        try:
            # APILAMOS SI ES UN ENTERO VÁLIDO
            elemento = int(input(f"Ingrese el valor a apilar: "))
            
            if elemento < 0:
                raise NoPositiveNumberException("Por favor, ingrese un número entero positivo.")
            else:
                pila.apilar(elemento)

            # DESAPILAMOS CUANDO LA CANTIDAD DE ELEMENTOS SEA MAYOR A TRES
            if len(pila.elementos) > 3:
                pila.desapilar()
            break
        except ValueError:
            print("[ERROR] Solamente están permitidos los valores enteros.")
        except NoPositiveNumberException as e:
            print(f"[ERROR] {e}")

print("\nElementos restantes en la pila:", pila.elementos)
input("Presione enter para cerrar el programa...")

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/08_stack/
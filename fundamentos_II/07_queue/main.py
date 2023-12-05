from queue import Queue

queue = Queue()

# SOLICITAR LOS VALORES AL USUARIO
for i in range(5):
    while True:
        try:
            # AGREGAR ELEMENTO A LA COLA
            element = int(input(f"Ingrese el elemento numérico {i + 1} para encolar: "))
            queue.push(element)

            # ELIMINAR PRIMER ELEMENTO DE LA COLA APLICANDO FIFO
            if (len(queue.items) > 2):
                queue.pop()
            break
        except ValueError:
            print("El valor a encolar debe ser un número entero.")

print("Elementos restantes en la cola", queue.items)

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/07_queue/
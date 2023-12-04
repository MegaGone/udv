from stack import Stack

stack = Stack()

# SOLICITAR LOS VALORES AL USUARIO
for i in range(5):
    while True:
        try:
            # AGREGAR ELEMENTO A LA PILA
            element = int(input(f"Ingrese el elemento numérico {i + 1} para apilar: "))
            stack.push(element)

            # ELIMINAR ELEMENTO DE LA PILA
            if (len(stack.items) > 2):
                stack.pop()
            break
        except ValueError:
            print("El valor a apilar debe ser un número.")

print("Elementos restantes en la pila", stack.items)

## Jimmy Martínez - Carné No. 202302745
## Repo - https://github.com/MegaGone/udv/blob/develop/fundamentos_II/07_stack/
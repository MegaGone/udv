int_primer_numero = 0
int_segundo_numero = 0
int_opcion = 0
float_resultado = 0

def validar_entero(valor):
    try:
        entero = int(valor)
        if entero <= 0:
            raise ValueError
        return entero
    except ValueError:
        return None

while True:
    try:
        int_primer_numero = int(input("Ingrese el primer número: "))
        int_segundo_numero = int(input("Ingrese el segundo número: "))
        break
    except ValueError:
        print("Los números ingresados no són válidos. Intente de nuevo.")

while int_opcion != 3:
    print("********************************************")
    print("1. Sumar los números")
    print("2. Restar los números")
    print("3. Salir")
    print("********************************************")
    
    int_opcion = input("\nSeleccione una opción: ")
    int_opcion = validar_entero(int_opcion)

    if int_opcion == 1:
        float_resultado = int_primer_numero + int_segundo_numero
        print(f"La suma de {int_primer_numero} y {int_segundo_numero} es:", float_resultado)
    elif int_opcion == 2:
        float_resultado = int_primer_numero - int_segundo_numero
        print(f"La resta de {int_primer_numero} y {int_segundo_numero} es:", float_resultado)
    elif int_opcion == 3:
        print("\n********************************************")
        print("Gracias por utilizar el programa")
        print("Nombres: Jimmy Javier")
        print("Apellidos: Martinez Sipac")
        print("Carne: 202302745")
        print("********************************************")
        input("Presione enter para cerrar el programa...")
    else:
        print("Opción inválida. Seleccione una opción del menú.")
    
## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/18_menu.py
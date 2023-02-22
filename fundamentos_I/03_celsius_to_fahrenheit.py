fahrenheit_degrees = 0
celsius_degrees = 0

while True:
    try:
        celsius_degrees = float(input("Ingrese un número: "))
        break
    except ValueError:
        print("Temperatura no válida. Intente nuevamente.")

fahrenheit_degrees = celsius_degrees * 1.8 + 32

print(f"{celsius_degrees} grados Celsius equivale a {fahrenheit_degrees} grados Fahrenheit.")
print("\nLink del análisis y diseño de la solución: shorturl.at/uQVW5")
input('Hecho por Jimmy Martínez - Carné No. 202302745')

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/03_celsius_to_fahrenheit.py
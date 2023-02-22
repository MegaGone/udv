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
print("Link del análisis y diseño de la solución: https://universidaddavincid-my.sharepoint.com/:b:/g/personal/202302745_estudiante_udv_edu_gt/ESNC8Jwru_1Ml51eKeEUrH4BgRiEfqf5Slp2Ov-J0FOk7A?e=amJ6Hd")
input('Hecho por Jimmy Martínez - Carné No. 202302745')

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/03_celsius_to_fahrenheit.py
# Declarar función sum_divisors(n):
#     declarar arr_int_divisors = []
#
#     Para cada i en rango(1, n):
#         Si n módulo i es igual a cero:
#             Agregar i a arr_int_divisors
#
#     Regresar la suma de arr_int_divisors

# Para cada i en rango(1, 10001):
#     long_sum1 = sum_divisors(i)
#     long_sum2 = sum_divisors(long_sum1)
#     Si i es igual a long_sum2 y long_sum1 no es igual a long_sum2:
#         Imprimir (i, long_sum1) son números amigos
#

def sum_divisors(n):
    arr_int_divisors = []
    for i in range(1, n):
        if n % i == 0:
            arr_int_divisors.append(i)
    return sum(arr_int_divisors)

for i in range(1, 10001):
    long_sum1 = sum_divisors(i)
    long_sum2 = sum_divisors(long_sum1)
    if i == long_sum2 and long_sum1 != long_sum2:
        print(f"({i}, {long_sum1}) son números amigos.")

## Jimmy Martínez - Carné No. 202302745
## REPO - https://github.com/MegaGone/udv/blob/develop/fundamentos_I/17_pairs_amicable_numbers.py
# Ejercicio 9: Programa que te dice si un número es primo o no primo.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

import math
import sys

num_to_check = input("Introduce un número (>=2) para comprobar si es primo: ")

# Verificar que el número sea válido (es un número entero y mayor o igual a 2)
if not num_to_check.isdigit() or int(num_to_check) < 2:
    print("ERROR. El número no es válido.", file=sys.stderr)
    exit(1)

# Convertir la entrada en un entero
num_to_check = int(num_to_check)

# Comprobar si el número es primo:
# Un número es primo si no tiene divisores en el rango [2, sqrt(num_to_check)]
is_prime = True
for i in range(2, int(math.sqrt(num_to_check)) + 1):
    if num_to_check % i == 0:
        is_prime = False
        break

# Mostrar el resultado
if is_prime:
    print("Es Primo")
else:
    print("No es Primo")

    
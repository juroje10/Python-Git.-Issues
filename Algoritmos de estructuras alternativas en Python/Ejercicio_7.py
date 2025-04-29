# Ejercicio 7: Programa que calcula la potencia según el exponente, considerando casos positivos, negativos o cero.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

base = float(input("Introduce la base: "))
exponent = int(input("Introduce el exponente: "))

if exponent > 0:
    result = base ** exponent
    print(f"El resultado es {result}.")
elif exponent == 0:
    print("El resultado es 1.")
else:
    result = 1 / (base ** abs(exponent))
    print(f"El resultado es {result}.")

# Ejercicio 6: Programa que calcula la potencia de un número real (base) elevado a un entero positivo (exponente)
# sin utilizar operadores de potencia.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

base = float(input("Introduce la base: "))
exponent = int(input("Introduce el exponente (entero positivo): "))

result = 1

for _ in range(exponent):
    result *= base

print(f"El resultado de {base} elevado a {exponent} es {result}")

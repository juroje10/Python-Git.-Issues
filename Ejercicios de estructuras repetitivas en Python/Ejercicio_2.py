# Ejercicio 2: Programa que solicita varios números y cuenta cuántos son mayores, menores o iguales a 0.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

quantity = int(input("¿Cuántos números deseas introducir? "))

greater_than_zero = 0
less_than_zero = 0
equal_to_zero = 0

for _ in range(quantity):
    num = float(input("Introduce un número: "))
    if num > 0:
        greater_than_zero += 1
    elif num < 0:
        less_than_zero += 1
    else:
        equal_to_zero += 1

print(f"Mayores que 0: {greater_than_zero}, Menores que 0: {less_than_zero}, Iguales a 0: {equal_to_zero}")

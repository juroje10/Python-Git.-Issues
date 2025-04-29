# Ejercicio 14: Calcula el precio final de un kilo de uva según su tipo y tamaño.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024
import sys

# Entrada de datos
type_grape = input("Introduce el tipo de uva (A/B): ").upper()
if type_grape != "A" and type_grape != "B":
    print("El tipo de uva introducido no es válido", file=sys.stderr)
    exit(1)

size = int(input("Introduce el tamaño de la uva (1/2): "))
if size != 1 and size != 2:
    print("El tamaño de uva introducido no es válido", file=sys.stderr)
    exit(1)

initial_price = float(input("Introduce el precio inicial por kilo de uva: "))

final_price = 0

# Cálculo del precio final
if type_grape == "A":
    if size == 1:
        final_price = initial_price + 0.20
    else:
        final_price = initial_price + 0.30
else:
    if size == 1:
        final_price = initial_price - 0.30
    else:
        final_price = initial_price - 0.50

print(f"El precio final por kilo de uva es: {final_price} euros.")

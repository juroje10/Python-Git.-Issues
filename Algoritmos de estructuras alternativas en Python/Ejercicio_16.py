# Ejercicio 16: Calcula el costo total de una llamada telefónica según su duración y el día o turno en que se realiza.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
duration = int(input("Introduce la duración de la llamada (minutos): "))
day = input("¿Es domingo? (s/n): ").lower()
shift = input("Introduce el turno (mañana/tarde): ").lower()

# Cálculo del costo base de la llamada
if duration <= 5:
    cost = duration * 1
elif duration <= 8:
    cost = 5 * 1 + (duration - 5) * 0.80
elif duration <= 10:
    cost = 5 * 1 + 3 * 0.80 + (duration - 8) * 0.70
else:
    cost = 5 * 1 + 3 * 0.80 + 2 * 0.70 + (duration - 10) * 0.50

# Cálculo del impuesto
if day == "s":
    tax = 0.03
elif shift == "mañana":
    tax = 0.15
else:
    tax = 0.10

# Costo final
total_cost = cost * (1 + tax)
print(f"El costo total de la llamada es: {total_cost} euros.")

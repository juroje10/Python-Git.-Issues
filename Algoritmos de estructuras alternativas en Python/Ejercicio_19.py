# Ejercicio 19: Muestra cuántos días tiene un mes basado en su número (del 1 al 12).
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
month = int(input("Introduce el número del mes (1 a 12): "))
days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

# Comprobación y resultado
if 1 <= month <= 12:
    print(f"El mes tiene {days_in_month[month]} días.")
else:
    print("ERROR: número incorrecto.")

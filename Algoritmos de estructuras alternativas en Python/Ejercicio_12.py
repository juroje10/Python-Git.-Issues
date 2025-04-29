# Ejercicio 12: Verifica si un año es bisiesto o no, basándose en las reglas del calendario.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
year = int(input("Introduce un año: "))

# Comprobación de si es bisiesto
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} es un año bisiesto.")
else:
    print(f"{year} no es un año bisiesto.")

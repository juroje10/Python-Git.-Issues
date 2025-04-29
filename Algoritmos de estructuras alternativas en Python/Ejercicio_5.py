# Ejercicio 5: Programa que lee la edad de dos personas y dice quién es más joven o si tienen la misma edad.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

age1 = int(input("Introduce la edad de la primera persona: "))
age2 = int(input("Introduce la edad de la segunda persona: "))

if age1 < age2:
    print("La primera persona es más joven.")
elif age1 > age2:
    print("La segunda persona es más joven.")
else:
    print("Ambas personas tienen la misma edad.")

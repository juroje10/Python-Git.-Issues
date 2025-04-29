# Ejercicio 4: Programa que pide dos números y muestra su división si el segundo no es cero.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

print("Introduce a continuación los número que quieras dividir -->")
print("-----------------------------------------------------------")

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num2 != 0:
    division = num1 / num2
    print(f"La división de {num1} entre {num2} es {division}.")
else:
    print("No se puede dividir por cero.")

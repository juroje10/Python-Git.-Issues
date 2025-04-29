# Ejercicio 10: Programa que cuenta cuántas veces aparece un carácter específico en una cadena ingresada por el usuario.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

string = input("Introduce una cadena: ")
character = input("Introduce el carácter a contar: ")

# Inicializamos el contador
occurrences = 0

# Usamos un bucle for para recorrer cada carácter en la cadena
for char in string:
    if char == character:
        occurrences += 1

print(f"El carácter '{character}' aparece {occurrences} veces en la cadena.")


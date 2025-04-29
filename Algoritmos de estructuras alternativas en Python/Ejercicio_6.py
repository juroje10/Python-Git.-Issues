# Ejercicio 6: Programa que lee una cadena por teclado y comprueba si es una letra mayúscula.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

character = input("Introduce un carácter: ")

if len(character) == 1 and character.isupper():
    print("Es una letra mayúscula.")
else:
    print("No es una letra mayúscula.")

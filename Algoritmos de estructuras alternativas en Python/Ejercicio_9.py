# Ejercicio 9: Programa que lee un carácter y determina si es un signo de puntuación, una letra, un dígito u otro carácter.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

character = input("Introduce un carácter: ")

if len(character) != 1:
    print("No es un carácter.")
elif character.isdigit():
    print("Es un dígito.")
elif character.isalpha():
    print("Es una letra.")
elif character in '.,;:!?¡¿-()[]{}"\'':
    print("Es signo de puntuación.")
else:
    print("Es otro carácter.")

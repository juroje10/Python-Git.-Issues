# Ejercicio 13: Programa que convierte las mayúsculas a minúsculas y viceversa en una cadena ingresada.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

text = input("Introduce una cadena: ")
converted_text = ""

for char in text:
    if char.isupper():
        converted_text += char.lower()
    elif char.islower():
        converted_text += char.upper()
    else:
        converted_text += char

print(f"Cadena convertida: {converted_text}")
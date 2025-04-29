# Ejercicio 15: Programa que determina si una cadena es un palíndromo, es decir, si se lee igual de adelante hacia atrás.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

text = input("Introduce una cadena: ").replace(" ", "").lower()

is_palindrome = True  # Suponemos que es un palíndromo inicialmente
length = len(text)

# Usamos un bucle for para comparar caracteres desde el inicio y el final
for i in range(length // 2):  # Solo necesitamos verificar hasta la mitad de la cadena
    if text[i] != text[length - 1 - i]:  # Comparamos el carácter actual con su par opuesto
        is_palindrome = False  # Si hay una diferencia, no es un palíndromo
        break  # Salimos del bucle si encontramos una diferencia

if is_palindrome:
    print("La cadena es un palíndromo.")
else:
    print("La cadena no es un palíndromo.")


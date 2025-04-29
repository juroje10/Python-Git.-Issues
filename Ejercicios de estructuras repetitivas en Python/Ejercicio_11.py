# Ejercicio 11: Programa que cuenta el número de palabras en una frase ingresada por el usuario.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

phrase = input("Introduce una frase: ").strip()

# Inicializamos el contador de palabras
word_count = 0

# Usamos un bucle for para contar las palabras
for word in phrase.split():  # split() separa la frase en palabras
    word_count += 1  # Incrementamos el contador por cada palabra encontrada

print(f"La frase tiene {word_count} palabras.")

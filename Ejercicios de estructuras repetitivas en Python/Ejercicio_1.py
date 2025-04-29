# Ejercicio 1: Programa que genera un número aleatorio y permite al usuario adivinarlo en hasta 10 intentos,
# indicando si el número es mayor o menor que la respuesta.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

import random

secret_number = random.randint(1, 100)
TRIES = 10

print("¡Adivina el número entre 1 y 100!")
for i in range(TRIES):
    guess = int(input(f"Intento {i + 1}/{TRIES}: "))

    if guess < secret_number:
            print("El número es mayor.")
    elif guess > secret_number:
            print("El número es menor.")
    else:
        print(f"¡Correcto! Has adivinado el número en {i + 1} intentos.")
        break

print(f"Lo siento, has agotado tus intentos. El número era {secret_number}.")



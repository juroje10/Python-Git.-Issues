"""
Programa que rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000
(ambos incluidos). A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Autor: Jesús Jurado Rodríguez
Fecha: 10/12/2024
"""

import sys
import random

# Constantes para las dimensiones del array
FILAS = 6
COLUMNAS = 10

# Inicialización del array
numbers = [[0] * COLUMNAS for _ in range(FILAS)]

# Variables para rastrear máximo y mínimo
minimo = sys.maxsize
fila_minimo = columna_minimo = 0

maximo = -sys.maxsize - 1
fila_maximo = columna_maximo = 0

# Encabezado de la tabla
print("\n      ", end="")
for columna in range(COLUMNAS):
    print(f"   {columna}  ", end="")
print()

print("    ┌" + "──────" * COLUMNAS + "┐")

# Rellenar el array y buscar máximo/mínimo
for fila in range(FILAS):
    print(f"  {fila} │", end="")
    for columna in range(COLUMNAS):
        # Generar número aleatorio entre 0 y 1000
        numbers[fila][columna] = random.randint(0, 1000)
        print(f"{numbers[fila][columna]:5d} ", end="")

        # Actualizar el mínimo
        if numbers[fila][columna] < minimo:
            minimo = numbers[fila][columna]
            fila_minimo, columna_minimo = fila, columna

        # Actualizar el máximo
        if numbers[fila][columna] > maximo:
            maximo = numbers[fila][columna]
            fila_maximo, columna_maximo = fila, columna
    print("│")

print("    └" + "──────" * COLUMNAS + "┘")

# Resultado final
print(f"\nEl máximo es {maximo} y está en la fila {fila_maximo}, columna {columna_maximo}")
print(f"El mínimo es {minimo} y está en la fila {fila_minimo}, columna {columna_minimo}")


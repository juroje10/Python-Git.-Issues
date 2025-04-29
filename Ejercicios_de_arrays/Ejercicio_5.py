"""
Rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
El programa genera números únicos en todo el array y, posteriormente, determina la posición del máximo y del mínimo.

Autor: Jesús Jurado Rodríguez
Fecha: 10/12/2024
"""

import random

# Constantes
ROWS = 6
COLUMNS = 10
LOWEST_NUM = 0
BIGGEST_NUM = 1000

# Generación del array con números únicos
array = [[None] * COLUMNS for _ in range(ROWS)]
unique_numbers = set()  # Almacena los números ya generados

for row in range(ROWS):
    for column in range(COLUMNS):
        while True:
            n = random.randint(LOWEST_NUM, BIGGEST_NUM)
            if n not in unique_numbers:  # Comprobar unicidad
                unique_numbers.add(n)
                array[row][column] = n
                break

# Impresión del array en formato tabular
print("\nArray generado:")
for row in array:
    print("  ".join(f"{num:4}" for num in row))

# Inicialización de variables para el máximo y el mínimo
max_num = LOWEST_NUM
min_num = BIGGEST_NUM
row_max, column_max = 0, 0
row_min, column_min = 0, 0

# Búsqueda del máximo y mínimo
for row in range(ROWS):
    for column in range(COLUMNS):
        num = array[row][column]
        if num > max_num:
            max_num, row_max, column_max = num, row, column
        if num < min_num:
            min_num, row_min, column_min = num, row, column

# Resultados
print(f"\nEl máximo de los números del array es {max_num}, y está en las posiciones ({row_max}, {column_max})")
print(f"El mínimo de los números del array es {min_num}, y está en las posiciones ({row_min}, {column_min})")

"""
Rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Autor: Jesús Jurado Rodríguez
Fecha: 10/12/2024
"""

import random

# Constantes
ROWS = 6
COLUMNS = 10
LOWEST_NUM = 0
BIGGEST_NUM = 1000

# Inicializamos el array y las variables para el máximo y mínimo
array = [[0] * COLUMNS for _ in range(ROWS)]
max_num = LOWEST_NUM
min_num = BIGGEST_NUM
max_position = (0, 0)
min_position = (0, 0)

# Rellenamos el array y calculamos el máximo y el mínimo en el mismo ciclo
for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = random.randint(LOWEST_NUM, BIGGEST_NUM)

        # Actualizamos el máximo
        if array[row][column] > max_num:
            max_num = array[row][column]
            max_position = (row, column)

        # Actualizamos el mínimo
        if array[row][column] < min_num:
            min_num = array[row][column]
            min_position = (row, column)

# Imprimimos el array en formato tabular
print("\nArray generado:")
for row in array:
    print("  ".join(f"{num:4}" for num in row))

# Mostramos resultados
print(f"\nEl máximo de los números del array es {max_num}, y está en las posiciones {max_position}")
print(f"El mínimo de los números del array es {min_num}, y está en las posiciones {min_position}")

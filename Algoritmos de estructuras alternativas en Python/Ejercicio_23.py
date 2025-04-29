# Ejercicio 23: Dado un conjunto de cinco números, determina cuál de los cuatro últimos es más cercano al primero.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
first_num = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))

# Cálculo de las diferencias
differences = {num2: abs(num2 - first_num), num3: abs(num3 - first_num), num4: abs(num4 - first_num), num5: abs(num5 - first_num)}

# Muestra el resultado
print(f"El número más cercano a {first_num} es: {}")

# Ejercicio 22: Pide cinco números enteros y determina cuál de ellos es el mayor.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
num4 = int(input("Introduce el cuarto número: "))
num5 = int(input("Introduce el quinto número: "))

# Determina el número mayor
max_num = max(num1, num2, num3, num4, num5)

# Muestra el resultado
print(f"El número mayor es: {max_num}")

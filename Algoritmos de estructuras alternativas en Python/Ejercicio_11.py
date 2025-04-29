# Ejercicio 11: Determina si un triángulo es rectángulo, equilátero, isósceles o escaleno según sus lados.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

print("Este programa indicará si un triángulo es rectángulo, equilátero, isósceles o escaleno según sus lados")
print("------------------------------------------------------------------------------------------------------")

# Entrada de datos
a = float(input("Introduce el lado A del triángulo: "))
b = float(input("Introduce el lado B del triángulo: "))
c = float(input("Introduce el lado C del triángulo: "))

# Comprobación del tipo de triángulo
if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
    print("Es un triángulo rectángulo.")
elif a == b == c:
    print("Es un triángulo equilátero.")
elif a == b or b == c or a == c:
    print("Es un triángulo isósceles.")
else:
    print("Es un triángulo escaleno.")

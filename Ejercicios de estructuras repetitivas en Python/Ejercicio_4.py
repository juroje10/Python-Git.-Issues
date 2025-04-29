# Ejercicio 4: Programa que muestra todos los números pares entre dos números dados por el usuario.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

start = int(input("Introduce el primer número: "))
end = int(input("Introduce el segundo número: "))

if end < start:
    start, end = end, start

if start % 2 != 0:
    start += 1

print("Números pares entre", start, "y", end)
print("------------------------------------")

for num in range(start, end + 1, 2):
    print(num, end=" ")

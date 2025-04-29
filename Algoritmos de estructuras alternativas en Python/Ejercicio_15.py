# Ejercicio 15: Calcula el costo total del viaje y el costo individual por alumno dependiendo del número de estudiantes.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

print("Calcular el coste de un viaje según los alumnos que vam")
print("-------------------------------------------------------")

# Entrada de datos
students = int(input("Introduce el número de alumnos: "))

# Cálculo de costos
if students >= 100:
    price_per_student = 65
elif students >= 50:
    price_per_student = 70
elif students >= 30:
    price_per_student = 95
else:
    price_per_student = 4000 / students

total_payment = students * price_per_student if students >= 30 else 4000
print(f"El total a pagar es {total_payment} euros y cada alumno pagará {price_per_student} euros.")

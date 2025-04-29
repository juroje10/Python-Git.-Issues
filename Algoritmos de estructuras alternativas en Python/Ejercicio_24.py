# Ejercicio 24: Convierte una calificación numérica de un examen en una calificación cualitativa.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
note = float(input("Introduce la calificación numérica: "))

# Determina la calificación cualitativa
if note < 5:
    qualitative_grade = "Suspenso"
elif 5 <= note < 7:
    qualitative_grade = "Aprobado"
elif 7 <= note < 9:
    qualitative_grade = "Notable"
elif 9 <= note < 10:
    qualitative_grade = "Sobresaliente"
elif note == 10:
    qualitative_grade = "Matrícula de Honor"
else:
    qualitative_grade = "Calificación inválida"

# Muestra el resultado
print(f"La calificación cualitativa es: {qualitative_grade}")

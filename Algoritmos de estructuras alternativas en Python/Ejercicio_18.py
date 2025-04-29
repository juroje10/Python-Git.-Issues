# Ejercicio 18: Muestra el nombre del día de la semana según el número ingresado (del 1 al 7).
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
day = int(input("Introduce un número del 1 al 7: "))
week_days = {1: "Lunes", 2: "Martes", 3: "Miércoles", 4: "Jueves", 5: "Viernes", 6: "Sábado", 7: "Domingo"}

# Comprobación y resultado
if 1 <= day <= 7:
    print(f"El día es {week_days[day]}.")
else:
    print("ERROR: número incorrecto.")

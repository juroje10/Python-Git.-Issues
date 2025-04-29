# Ejercicio 8: Programa que pide una nota, una edad y un sexo, y muestra si es ACEPTADA, POSIBLE o NO ACEPTADA.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

note = float(input("Introduce la nota: "))
age = int(input("Introduce la edad: "))
gender = input("Introduce el sexo (M/F): ").upper()

if note >= 5 and age >= 18:
    if gender == 'F':
        print("ACEPTADA")
    elif gender == 'M':
        print("POSIBLE")
    else:
        print("Sexo no válido.")
else:
    print("NO ACEPTADA")

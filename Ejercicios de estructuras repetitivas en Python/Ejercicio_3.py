# Ejercicio 3: Programa que identifica si el carácter ingresado es una vocal o no. Finaliza al introducir un espacio.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

while True:
    character = input("Introduce un carácter (espacio para salir): ")
    if character == ' ':
        break
    elif character in 'aáAÁeéEÉiíIÍoóOÓuúUÚ':
        print("VOCAL")
    else:
        print("NO VOCAL")

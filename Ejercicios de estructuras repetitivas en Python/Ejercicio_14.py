# Ejercicio 14: Programa que verifica si una cadena contiene una subcadena, ambas introducidas por el usuario.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

main_string = input("Introduce la cadena principal: ")
substring = input("Introduce la subcadena a buscar: ")

# Inicializamos una variable para verificar la presencia de la subcadena
found = False
substring_length = len(substring)
main_string_length = len(main_string)

# Usamos un bucle for para recorrer la cadena principal
for i in range(main_string_length - substring_length + 1):
    if main_string[i:i + substring_length] == substring:  # Comparamos la parte de la cadena con la subcadena
        found = True  # Si encontramos la subcadena, cambiamos el estado
        break  # Salimos del bucle, ya que encontramos la subcadena

if found:
    print("La subcadena está presente en la cadena principal.")
else:
    print("La subcadena no está presente en la cadena principal.")

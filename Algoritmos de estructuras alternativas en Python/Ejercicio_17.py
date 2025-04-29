# Ejercicio 17: Muestra la cara opuesta de un dado basado en el número que ha salido.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
face = int(input("Introduce el número del dado (1 a 6): "))
opposite_faces = {1: "seis", 2: "cinco", 3: "cuatro", 4: "tres", 5: "dos", 6: "uno"}

# Comprobación y resultado
if 1 <= face <= 6:
    print(f"En la cara opuesta está el '{opposite_faces[face]}'.")
else:
    print("ERROR: número incorrecto.")

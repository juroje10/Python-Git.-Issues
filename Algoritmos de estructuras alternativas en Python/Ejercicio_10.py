# Ejercicio 10: Este programa clasifica dos circunferencias como exteriores, tangentes, secantes, interiores o concéntricas según sus radios y la distancia entre sus centros.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 15/10/2024

import math

# Solicitar los puntos centrales y los radios
x1 = float(input("Ingrese la coordenada x del centro de la primera circunferencia (x1): "))
y1 = float(input("Ingrese la coordenada y del centro de la primera circunferencia (y1): "))
r1 = float(input("Ingrese el radio de la primera circunferencia (r1): "))

x2 = float(input("Ingrese la coordenada x del centro de la segunda circunferencia (x2): "))
y2 = float(input("Ingrese la coordenada y del centro de la segunda circunferencia (y2): "))
r2 = float(input("Ingrese el radio de la segunda circunferencia (r2): "))

# Calcular la distancia entre los centros de las circunferencias
distancia_centros = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Determinar la relación entre las circunferencias
if distancia_centros > r1 + r2:
    print("Las circunferencias son exteriores.")
elif distancia_centros == r1 + r2:
    print("Las circunferencias son tangentes exteriores.")
elif distancia_centros < r1 + r2 and distancia_centros > abs(r1 - r2):
    print("Las circunferencias son secantes.")
elif distancia_centros == abs(r1 - r2):
    print("Las circunferencias son tangentes interiores.")
elif distancia_centros < abs(r1 - r2):
    print("Una circunferencia está dentro de la otra (interiores).")
elif distancia_centros == 0 and r1 == r2:
    print("Las circunferencias son concéntricas.")
else:
    print("Error en los datos ingresados.")

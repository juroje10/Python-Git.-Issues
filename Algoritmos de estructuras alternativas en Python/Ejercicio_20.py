# Ejercicio 20: Calcula el costo de envío de un paquete según su peso y la zona de destino.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
weight = float(input("Introduce el peso del paquete en kg: "))
zone = int(input("Introduce la zona de envío (1-5): "))

# Comprobación de peso
if weight > 5:
    print("Paquete rechazado por sobrepeso.")
else:
    # Costo por gramo según la zona
    shipping_costs = {1: 24, 2: 20, 3: 21, 4: 10, 5: 18}
    shipping_cost = weight * 1000 * shipping_costs[zone]
    print(f"El costo del envío es: {shipping_cost} euros.")

# Ejercicio 13: Descompone una cantidad de euros en el menor número posible de billetes y monedas.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 19/10/2024

# Entrada de datos
amount = int(input("Introduce la cantidad de euros: "))
bills_coins = [500, 200, 100, 50, 20, 10, 5, 2, 1]
result = []

# Cálculo del desglose
for value in bills_coins:
    bill_count = amount // value
    if bill_count > 0:
        result.append(f"{bill_count} de {value}€")
        amount %= value

# Mostrar resultado
print("\n".join(result))

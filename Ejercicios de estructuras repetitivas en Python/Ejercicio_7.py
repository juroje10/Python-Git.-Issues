# Ejercicio 7: Programa que calcula el pago mensual y el total a pagar de un producto cuyo costo se duplica
# cada mes durante 20 meses.
# Autor --> Jesús Jurado Rodríguez
# Fecha --> 26/10/2024

INITIAL_PAYMENT = 10
MONTHS = 20

total = 0
current_payment = INITIAL_PAYMENT

for month in range(1, MONTHS + 1):
    total += current_payment
    print(f"Mes {month}: {current_payment} €")
    current_payment *= 2

print(f"El total pagado en 20 meses es: {total} €")

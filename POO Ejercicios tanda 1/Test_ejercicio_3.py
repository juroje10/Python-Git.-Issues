"""
Prueba de la clase "Rectángulo".
"""

from Ejercicio_2 import Point
from Ejercicio_3 import Rectangle

p1 = Point(2, 5)
p2 = Point(5, 10)

my_rectangle = Rectangle(p1, p2)
print(f"El área de {my_rectangle} es {my_rectangle.area} y el perímetro es {my_rectangle.perimeter}")
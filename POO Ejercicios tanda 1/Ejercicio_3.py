"""
Implementa la clase Rectángulo (determinado por dos objetos Point) que además de su constructor, tendrá dos métodos
para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree
dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

Autor: Jesús Jurado Rodríguez.
Fecha: 22/01/2025.
"""
from Ejercicio_2 import Point
from typeguard import typechecked

@typechecked
class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, value: Point):
        self.__p1 = value

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, value: Point):
        self.__p2 = value

    @property
    def area(self):
        return abs((self.__p1.x - self.__p2.x) * (self.__p1.y - self.__p2.y))

    @property
    def perimeter(self):
        return 2 * abs(self.__p1.x - self.__p2.x) + 2 * abs(self.__p1.y - self.__p2.y)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__p1}, {self.__p2})"

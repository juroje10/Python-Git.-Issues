"""
Clase que representa una fracción de forma que podamos hacer las siguientes operaciones:

- Construir un objeto con el numerador y el denominador. La fracción se crea simplificada, no se puede dividir por 0.
- Obtener resultado de la fracción (número real).
- Mediante sobrecarga de operadores:
  * Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
  * Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).
  * Comparar fracciones.

Autor: Jesús Jurado Rodríguez
Fecha: 04/03/2025
"""

from __future__ import annotations
import math
from typeguard import typechecked


@typechecked
class Fraction:

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ZeroDivisionError("Una fracción no puede tener 0 como denominador.")
        gcd = math.gcd(numerator, denominator)
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    @property
    def numerator(self):
        return self._numerator

    @property
    def denominator(self):
        return self._denominator

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._numerator, self._denominator})"

    def value(self):
        return self._numerator / self._denominator

    def __mul__(self, other: (int, Fraction)):
        if isinstance(other, int):
            return Fraction(self._numerator * other, self._denominator)
        return Fraction(self._numerator * other._numerator, self._denominator * other._denominator)

    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return self * -1

    def __add__(self, other: Fraction):
        return Fraction(self._numerator * other._denominator + self._denominator * other._numerator, self._denominator * other._denominator)

    def __sub__(self, other: Fraction):
        return self + -other

    def __truediv__(self, other: Fraction):
        return Fraction(self._numerator * other._denominator, self._denominator * other._numerator)

    def __eq__(self, other: Fraction):
        return (self._numerator, self._denominator) == (other._numerator, other._denominator)

    def __ne__(self, other: Fraction):
        return not (self == other)

    def __lt__(self, other: Fraction):
        return self._numerator * other._denominator < other._numerator * self._denominator

    def __le__(self, other: Fraction):
        return self < other or self == other

    def __gt__(self, other: Fraction):
        return not (self <= other)

    def __ge__(self, other: Fraction):
        return not (self < other)

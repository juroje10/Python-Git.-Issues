"""
Clase que almacena duraciones de tiempo. Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

- t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
- t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
- t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Tiene getters y setters mediante propiedades y métodos para:

- Sumar y restar objetos de la clase (el resultado es otro objeto).
- Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea '10h 35m 5s'

Aunque el ejercicio no lo pide, hemos implementado también la posibilidad de aplicar operaciones relacionales sobre
los objetos de esta clase sobrecargando los métodos correspondientes.

Autor: Jesús Jurado Rodríguez
Fecha: 03/03/2025
"""

from __future__ import annotations
from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):  # solo se recibe un parámetro
            other = hours
            self._hours, self._minutes, self._seconds = other._hours, other._minutes, other._seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self._hours, self._minutes, self._seconds = hours, minutes, seconds
            self._normalize()
        else:
            raise TypeError("Debe crearse un objeto Duración con tres enteros u otro objeto Duración")

    def _normalize(self):
        total_seconds = self._total_seconds()
        if total_seconds < 0:
            raise ValueError("No se permiten duraciones negativas")
        self._hours = total_seconds // 3600
        self._minutes = (total_seconds % 3600) // 60
        self._seconds = total_seconds % 3600 % 60

    def _total_seconds(self):
        return self._hours * 3600 + self._minutes * 60 + self._seconds

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value: int):
        aux = Duration(value, self._minutes, self._seconds)
        self._hours, self._minutes, self._seconds = aux._hours, aux._minutes, aux._seconds

    @property
    def minutes(self):
        return self._minutes

    @minutes.setter
    def minutes(self, value: int):
        aux = Duration(self._hours, value, self._seconds)
        self._hours, self._minutes, self._seconds = aux._hours, aux._minutes, aux._seconds

    @property
    def seconds(self):
        return self._seconds

    @seconds.setter
    def seconds(self, value: int):
        aux = Duration(self.hours, self.minutes, value)
        self._hours, self._minutes, self._seconds = aux._hours, aux._minutes, aux._seconds

    def add_seconds(self, seconds: int):
        self.seconds += seconds

    def sub_seconds(self, seconds: int):
        self.seconds -= seconds

    def add_minutes(self, minutes: int):
        self.minutes += minutes

    def sub_minutes(self, minutes: int):
        self.minutes -= minutes

    def add_hours(self, hours: int):
        self.hours += hours

    def sub_hours(self, hours: int):
        self.hours -= hours

    def __str__(self):
        return f"{self._hours}h {self._minutes}m {self._seconds}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._hours}, {self._minutes}, {self._seconds})"

    # Sobrecarga de operadores

    def __add__(self, other: Duration):
        return Duration(self._hours + other._hours, self._minutes + other._minutes,
                        self._seconds + other._seconds)

    def __sub__(self, other: Duration):
        return Duration(self._hours - other._hours, self._minutes - other._minutes,
                        self._seconds - other._seconds)

    def __eq__(self, other: Duration):
        return (self._hours, self._minutes, self._seconds) == (other._hours, other._minutes, other._seconds)

    def __ne__(self, other: Duration):
        return not self == other

    def __lt__(self, other: Duration):
        return self._total_seconds() < other._total_seconds()

    def __le__(self, other: Duration):
        return self._total_seconds() <= other._total_seconds()

    def __gt__(self, other: Duration):
        return not self <= other

    def __ge__(self, other: Duration):
        return not self < other

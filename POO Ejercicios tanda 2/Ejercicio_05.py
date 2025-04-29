"""
Clase que representa una estructura de datos tipo cola (queue).

Funciones principales:
- Crear la cola con o sin valores iniciales o a partir de otra cola.
- Obtener el número de elementos almacenados.
- Comprobar si la cola está vacía.
- Vaciar la cola por completo.
- Encolar un elemento (enqueue).
- Desencolar un elemento (dequeue) devolviendo y eliminando el primero.
- Consultar el primer elemento sin eliminarlo (front).

Autor: Jesús Jurado Rodríguez
Fecha: 02/03/2025
"""
from typeguard import typechecked

@typechecked
class Queue:

    def __init__(self, *values):
        if len(values) == 1 and isinstance(values[0], Queue):
            self.__values = values[0].__values.copy()
        else:
            self.__values = list(values)

    def __repr__(self):
        return f"{self.__class__.__name__}(values={self.__values})"

    def __str__(self):
        return str(self.__values)

    @property
    def size(self):
        return len(self.__values)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.__values.clear()

    def enqueue(self, value):
        self.__values.append(value)

    def dequeue(self):
        return self.__values.pop(0)

    def front(self):
        return self.__values[0]

if __name__ == '__main__':
    queue1 = Queue(1, 2, 3, 4, 5)
    queue2 = Queue(queue1)
    print(f"Creadas {queue1} y {queue2}")

    print(f"Encolo 'A' y 'B' en {queue1}")
    queue1.enqueue('A')
    queue1.enqueue('B')
    print("Resultado:", queue1)

    print(f"Desencolo dos elementos de {queue2}")
    print(f"Desencolo {queue2.dequeue()}, {queue2.dequeue()}")
    print("Resultado:", queue2)

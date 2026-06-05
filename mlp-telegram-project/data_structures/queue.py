"""
--------

Implementación de una estructura de datos Cola (Queue) siguiendo el
principio FIFO (First In, First Out).

Una cola es una estructura lineal en la que el primer elemento que
ingresa es el primero en salir. Este comportamiento es ampliamente
utilizado en sistemas operativos, planificación de procesos,
algoritmos de búsqueda, simulaciones y procesamiento de eventos.

Este módulo forma parte del conjunto de estructuras de datos utilizadas
en el proyecto de clasificación de complejidad algorítmica mediante
Redes Neuronales Multicapa (MLP).

Arquitectura:
-------------
            ENQUEUE
               │
               ▼
    ┌─────────────────────┐
    │ A │ B │ C │ D │ E │
    └─────────────────────┘
      ▲
      │
   DEQUEUE

FIFO:
-----
First In  → First Out

Ejemplo:

enqueue(A)
enqueue(B)
enqueue(C)

dequeue() → A
dequeue() → B
dequeue() → C

Operaciones soportadas:
-----------------------
- enqueue(item)
- dequeue()
- is_empty()
- size()

Tecnologías utilizadas:
-----------------------
- Python
- Data Structures
- FIFO Queue

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""


class Queue:
    """
    Implementación básica de una Cola (Queue).

    La estructura sigue el principio FIFO
    (First In, First Out), donde el primer
    elemento insertado es el primero en ser removido.

    Attributes
    ----------
    items : list
        Lista interna utilizada para almacenar
        los elementos de la cola.
    """

    def __init__(self):
        """
        Inicializa una cola vacía.

        Se crea una lista interna donde se almacenarán
        los elementos ingresados.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        self.items = []

    def enqueue(
        self,
        item
    ):
        """
        Inserta un nuevo elemento al final de la cola.

        Parameters
        ----------
        item : Any
            Elemento que será agregado a la cola.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        self.items.append(
            item
        )

    def dequeue(
        self
    ):
        """
        Remueve y retorna el primer elemento de la cola.

        Si la cola se encuentra vacía,
        retorna None.

        Returns
        -------
        Any
            Primer elemento de la cola.

        None
            Si la cola está vacía.

        Time Complexity
        ---------------
        O(n)

        Debido a que list.pop(0) desplaza todos
        los elementos restantes una posición.

        Space Complexity
        ----------------
        O(1)
        """

        if not self.is_empty():

            return (
                self.items.pop(0)
            )

        return None

    def is_empty(
        self
    ):
        """
        Verifica si la cola está vacía.

        Returns
        -------
        bool
            True si la cola no contiene elementos.
            False en caso contrario.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        return (
            len(self.items)
            == 0
        )

    def size(
        self
    ):
        """
        Retorna la cantidad de elementos almacenados
        actualmente en la cola.

        Returns
        -------
        int
            Número de elementos presentes.

        Time Complexity
        ---------------
        O(1)

        Space Complexity
        ----------------
        O(1)
        """

        return len(
            self.items
        )


if __name__ == "__main__":
    """
    Ejemplo de uso de la estructura Queue.
    """

    queue = Queue()

    print("¿Cola vacía?:", queue.is_empty())

    queue.enqueue("Cristian")
    queue.enqueue("Katherine")
    queue.enqueue("MLP")

    print("Tamaño:", queue.size())

    print("Sale:", queue.dequeue())
    print("Sale:", queue.dequeue())

    print("Tamaño actual:", queue.size())

    print("¿Cola vacía?:", queue.is_empty())
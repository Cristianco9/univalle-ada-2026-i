"""
Pruebas unitarias para la estructura de datos Queue ubicada en
data_structures/queue.py.

Autor:
- Cristian Cortes
"""

# Framework utilizado para ejecutar las pruebas unitarias
import pytest

# Clase Queue que será evaluada
from data_structures.queue import Queue


# ─────────────────────────────────────────────────────────────────────────────
# HAPPY PATH TESTS
# Casos de uso esperados donde la cola funciona correctamente.
# ─────────────────────────────────────────────────────────────────────────────

class TestQueueHappyPath:

    def test_new_queue_is_empty(self):
        """
        Verifica que una cola recién creada esté vacía.
        """
        q = Queue()

        assert q.is_empty() is True

    def test_size_after_enqueue(self):
        """
        Verifica que el tamaño aumente después de insertar elementos.
        """
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)

        assert q.size() == 2

    def test_is_empty_false_after_enqueue(self):
        """
        Verifica que la cola deje de estar vacía después
        de insertar un elemento.
        """
        q = Queue()

        q.enqueue("x")

        assert q.is_empty() is False

    def test_fifo_order_three_elements(self):
        """
        Verifica el comportamiento FIFO
        (First In, First Out).

        El primer elemento insertado debe ser
        el primero en salir.
        """
        q = Queue()

        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)

        assert q.dequeue() == 10
        assert q.dequeue() == 20
        assert q.dequeue() == 30

    def test_size_decreases_after_dequeue(self):
        """
        Verifica que el tamaño disminuya después
        de extraer un elemento.
        """
        q = Queue()

        q.enqueue("a")
        q.enqueue("b")

        q.dequeue()

        assert q.size() == 1

    def test_is_empty_after_all_dequeued(self):
        """
        Verifica que la cola vuelva a estar vacía
        cuando todos los elementos han sido removidos.
        """
        q = Queue()

        q.enqueue(1)

        q.dequeue()

        assert q.is_empty() is True

    def test_enqueue_various_types(self):
        """
        Verifica que la cola pueda almacenar
        diferentes tipos de datos.
        """
        q = Queue()

        q.enqueue(42)
        q.enqueue("hello")
        q.enqueue([1, 2, 3])
        q.enqueue({"key": "value"})

        assert q.size() == 4

        assert q.dequeue() == 42
        assert q.dequeue() == "hello"

    def test_interleaved_enqueue_dequeue(self):
        """
        Verifica operaciones alternadas de inserción
        y extracción manteniendo el orden FIFO.
        """
        q = Queue()

        q.enqueue(1)
        q.enqueue(2)

        assert q.dequeue() == 1

        q.enqueue(3)

        assert q.dequeue() == 2
        assert q.dequeue() == 3

    def test_size_of_empty_queue_is_zero(self):
        """
        Verifica que una cola vacía tenga tamaño 0.
        """
        q = Queue()

        assert q.size() == 0

    def test_batch_tuples_workflow(self):
        """
        Simula el caso de uso del batch loader
        utilizado durante el entrenamiento del MLP.

        Cada elemento de la cola contiene un batch:
        (X_batch, y_batch)
        """
        q = Queue()

        batches = [
            ([1, 2], [0, 1]),
            ([3, 4], [1, 0]),
            ([5, 6], [0, 1])
        ]

        for batch in batches:
            q.enqueue(batch)

        assert q.size() == 3

        assert q.dequeue() == ([1, 2], [0, 1])


# ─────────────────────────────────────────────────────────────────────────────
# EDGE CASE TESTS
# Casos límite y escenarios poco comunes.
# ─────────────────────────────────────────────────────────────────────────────

class TestQueueEdgeCases:

    def test_dequeue_from_empty_returns_none(self):
        """
        Verifica que intentar extraer de una cola vacía
        retorne None.
        """
        q = Queue()

        assert q.dequeue() is None

    def test_dequeue_until_empty_then_dequeue_again(self):
        """
        Verifica que múltiples llamadas a dequeue()
        sobre una cola vacía sigan retornando None.
        """
        q = Queue()

        q.enqueue("only")

        q.dequeue()

        assert q.dequeue() is None

    def test_enqueue_none_value(self):
        """
        Verifica que la cola pueda almacenar
        el valor None.
        """
        q = Queue()

        q.enqueue(None)

        assert q.size() == 1
        assert q.dequeue() is None

    def test_enqueue_false_value(self):
        """
        Verifica que la cola pueda almacenar
        valores booleanos False.
        """
        q = Queue()

        q.enqueue(False)

        assert q.dequeue() is False

    def test_enqueue_zero(self):
        """
        Verifica que la cola pueda almacenar
        el valor numérico 0.
        """
        q = Queue()

        q.enqueue(0)

        assert q.dequeue() == 0

    def test_large_queue_maintains_fifo(self):
        """
        Verifica el comportamiento FIFO en una cola
        de gran tamaño.
        """
        q = Queue()

        n = 1000

        for i in range(n):
            q.enqueue(i)

        for i in range(n):
            assert q.dequeue() == i

    def test_single_element_enqueue_dequeue_cycle(self):
        """
        Verifica múltiples ciclos de inserción
        y extracción de un único elemento.
        """
        q = Queue()

        for value in [1, 2, 3]:

            q.enqueue(value)

            assert q.dequeue() == value

            assert q.is_empty() is True

    def test_items_list_is_initialized_empty(self):
        """
        Verifica que la lista interna utilizada por
        la cola se inicialice vacía.
        """
        q = Queue()

        assert q.items == []
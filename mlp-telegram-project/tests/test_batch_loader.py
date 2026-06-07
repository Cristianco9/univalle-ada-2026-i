"""
Pruebas unitarias para batch_loader.py

Se valida:

- Creación correcta de batches
- Cantidad de batches generados
- Batch incompleto final
- Dataset vacío
- batch_size = 1
- batch_size mayor que el dataset
- Preservación del orden
- Correspondencia X-y

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

from utils.batch_loader import create_batches


# ==========================================================
# CASO BÁSICO
# ==========================================================

def test_batch_count_basic():
    """
    Debe generar la cantidad correcta de batches.
    """

    X = [1, 2, 3, 4, 5]
    y = [0, 0, 1, 1, 1]

    queue = create_batches(X, y, batch_size=2)

    assert queue.size() == 3


# ==========================================================
# ÚLTIMO BATCH INCOMPLETO
# ==========================================================

def test_last_batch_smaller():
    """
    El último batch puede tener menos elementos.
    """

    X = [1, 2, 3, 4, 5]
    y = [0, 0, 1, 1, 1]

    queue = create_batches(X, y, batch_size=2)

    queue.dequeue()
    queue.dequeue()

    last_batch = queue.dequeue()

    batch_X, batch_y = last_batch

    assert len(batch_X) == 1
    assert len(batch_y) == 1


# ==========================================================
# DATASET VACÍO
# ==========================================================

def test_empty_dataset():
    """
    Dataset vacío debe producir una cola vacía.
    """

    queue = create_batches([], [], batch_size=4)

    assert queue.size() == 0


# ==========================================================
# BATCH SIZE = 1
# ==========================================================

def test_batch_size_one():
    """
    Cada elemento debe convertirse en un batch individual.
    """

    X = [10, 20, 30]
    y = [0, 1, 0]

    queue = create_batches(X, y, batch_size=1)

    assert queue.size() == 3


# ==========================================================
# BATCH SIZE MAYOR AL DATASET
# ==========================================================

def test_batch_size_larger_than_dataset():
    """
    Si batch_size supera el tamaño del dataset,
    debe generarse un único batch.
    """

    X = [1, 2, 3]
    y = [0, 1, 0]

    queue = create_batches(X, y, batch_size=10)

    assert queue.size() == 1


# ==========================================================
# PRESERVACIÓN DEL ORDEN
# ==========================================================

def test_preserve_order():
    """
    Los elementos deben conservar su orden original.
    """

    X = [1, 2, 3, 4]
    y = [10, 20, 30, 40]

    queue = create_batches(X, y, batch_size=2)

    batch_X, batch_y = queue.dequeue()

    assert batch_X == [1, 2]
    assert batch_y == [10, 20]


# ==========================================================
# CORRESPONDENCIA X-Y
# ==========================================================

def test_x_y_alignment():
    """
    Cada muestra debe conservar su etiqueta asociada.
    """

    X = ["a", "b", "c", "d"]
    y = [1, 2, 3, 4]

    queue = create_batches(X, y, batch_size=2)

    batch_X, batch_y = queue.dequeue()

    assert batch_X[0] == "a"
    assert batch_y[0] == 1

    assert batch_X[1] == "b"
    assert batch_y[1] == 2


# ==========================================================
# CONSUMO COMPLETO DE LA COLA
# ==========================================================

def test_dequeue_all_batches():
    """
    Debe poder consumirse toda la cola sin errores.
    """

    X = [1, 2, 3, 4]
    y = [0, 0, 1, 1]

    queue = create_batches(X, y, batch_size=2)

    first = queue.dequeue()
    second = queue.dequeue()

    assert first is not None
    assert second is not None
    assert queue.dequeue() is None


# ==========================================================
# LISTA ORIGINAL NO MODIFICADA
# ==========================================================

def test_original_data_not_modified():
    """
    La función no debe modificar las listas originales.
    """

    X = [1, 2, 3, 4]
    y = [0, 1, 0, 1]

    original_X = X.copy()
    original_y = y.copy()

    create_batches(X, y, batch_size=2)

    assert X == original_X
    assert y == original_y


# ==========================================================
# DATASET DE UN SOLO ELEMENTO
# ==========================================================

def test_single_element_dataset():
    """
    Debe funcionar correctamente con un único registro.
    """

    X = [42]
    y = [1]

    queue = create_batches(X, y, batch_size=4)

    assert queue.size() == 1

    batch_X, batch_y = queue.dequeue()

    assert batch_X == [42]
    assert batch_y == [1]
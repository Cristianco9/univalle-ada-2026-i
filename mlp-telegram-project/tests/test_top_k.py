"""
Pruebas unitarias para los algoritmos Top-K.

Se valida:

- Casos básicos
- Duplicados
- Números negativos
- k = 0
- k = tamaño lista
- k mayor que tamaño lista
- Lista vacía
- Consistencia entre implementaciones

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

from algorithms.top_k import (
    top_k_heap,
    top_k_sort
)


# ==========================================================
# CASOS BÁSICOS
# ==========================================================

def test_top_k_heap_basic():
    """
    Debe retornar los 2 valores más grandes usando heap.
    """

    data = [1, 5, 2, 9, 3]

    result = top_k_heap(data, 2)

    assert sorted(result) == [5, 9]


def test_top_k_sort_basic():
    """
    Debe retornar los 2 valores más grandes usando sort.
    """

    data = [1, 5, 2, 9, 3]

    result = top_k_sort(data, 2)

    assert sorted(result) == [5, 9]


# ==========================================================
# DUPLICADOS
# ==========================================================

def test_top_k_with_duplicates():
    """
    Debe conservar valores duplicados si pertenecen al Top-K.
    """

    data = [10, 10, 8, 5, 1]

    heap_result = top_k_heap(data, 2)
    sort_result = top_k_sort(data, 2)

    assert sorted(heap_result) == [10, 10]
    assert sorted(sort_result) == [10, 10]


# ==========================================================
# NEGATIVOS
# ==========================================================

def test_top_k_negative_values():
    """
    Debe funcionar correctamente con números negativos.
    """

    data = [-10, -3, -7, -1]

    heap_result = top_k_heap(data, 2)
    sort_result = top_k_sort(data, 2)

    assert sorted(heap_result) == [-3, -1]
    assert sorted(sort_result) == [-3, -1]


# ==========================================================
# K = 0
# ==========================================================

def test_k_zero():
    """
    Si k es cero debe retornar una colección vacía.
    """

    data = [1, 2, 3]

    assert top_k_heap(data, 0) == []
    assert top_k_sort(data, 0) == []


# ==========================================================
# K = N
# ==========================================================

def test_k_equals_length():
    """
    Si k es igual al tamaño de la lista,
    debe retornar todos los elementos.
    """

    data = [5, 1, 3]

    heap_result = top_k_heap(data, len(data))
    sort_result = top_k_sort(data, len(data))

    assert sorted(heap_result) == sorted(data)
    assert sorted(sort_result) == sorted(data)


# ==========================================================
# K > N
# ==========================================================

def test_k_greater_than_length():
    """
    Si k es mayor que el tamaño de la lista,
    debe retornar todos los elementos disponibles.
    """

    data = [4, 2]

    heap_result = top_k_heap(data, 10)
    sort_result = top_k_sort(data, 10)

    assert sorted(heap_result) == [2, 4]
    assert sorted(sort_result) == [2, 4]


# ==========================================================
# LISTA VACÍA
# ==========================================================

def test_empty_list():
    """
    Debe manejar listas vacías sin errores.
    """

    assert top_k_heap([], 3) == []
    assert top_k_sort([], 3) == []


# ==========================================================
# CONSISTENCIA ENTRE IMPLEMENTACIONES
# ==========================================================

def test_heap_and_sort_return_same_result():
    """
    Ambas implementaciones deben producir
    el mismo conjunto de elementos.
    """

    data = [7, 1, 9, 3, 4, 8]

    heap_result = top_k_heap(data, 3)
    sort_result = top_k_sort(data, 3)

    assert sorted(heap_result) == sorted(sort_result)


# ==========================================================
# LISTA ORIGINAL NO MODIFICADA
# ==========================================================

def test_original_list_not_modified():
    """
    Los algoritmos no deben modificar la lista original.
    """

    data = [5, 2, 9, 1]
    original = data.copy()

    top_k_heap(data, 2)
    top_k_sort(data, 2)

    assert data == original


# ==========================================================
# TOP-1
# ==========================================================

def test_top_one():
    """
    Debe retornar únicamente el valor máximo.
    """

    data = [4, 9, 2, 7]

    heap_result = top_k_heap(data, 1)
    sort_result = top_k_sort(data, 1)

    assert heap_result == [9]
    assert sort_result == [9]
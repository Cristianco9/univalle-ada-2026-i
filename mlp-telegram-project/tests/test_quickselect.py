"""
Pruebas unitarias para las funciones:

- partition()
- quickselect()
- find_median()

implementadas en algorithms/quickselect.py

Autor:
- Cristian Cortes

Objetivo:
Validar el correcto funcionamiento del algoritmo Quickselect y de la
función auxiliar partition(), verificando casos normales, casos límite
y la correcta obtención de la mediana.
"""

# Framework utilizado para ejecutar las pruebas unitarias
import pytest

# Funciones que serán evaluadas
from algorithms.quickselect import (
    partition,
    quickselect,
    find_median
)


# ─────────────────────────────────────────────────────────────────────────────
# TESTS DE partition()
# ─────────────────────────────────────────────────────────────────────────────

class TestPartition:
    """
    Pruebas para la función partition().

    Esta función reorganiza el arreglo tomando el último elemento
    como pivote y ubicándolo en su posición definitiva.
    """

    def test_pivot_lands_at_correct_index(self):
        """
        Verifica que el pivote termine en la posición correcta.

        Todos los elementos a la izquierda deben ser menores o iguales
        al pivote y todos los elementos a la derecha mayores o iguales.
        """
        arr = [3, 1, 4, 1, 5]

        idx = partition(arr, 0, len(arr) - 1)

        pivot = arr[idx]

        assert all(arr[i] <= pivot for i in range(idx))
        assert all(arr[i] >= pivot for i in range(idx + 1, len(arr)))

    def test_single_element_returns_0(self):
        """
        Verifica que un arreglo de un solo elemento
        retorne índice 0.
        """
        arr = [7]

        assert partition(arr, 0, 0) == 0

    def test_already_sorted(self):
        """
        Verifica el comportamiento cuando el arreglo
        ya está ordenado.
        """
        arr = [1, 2, 3, 4, 5]

        idx = partition(arr, 0, len(arr) - 1)

        pivot = arr[idx]

        assert all(arr[i] <= pivot for i in range(idx))

    def test_reverse_sorted(self):
        """
        Verifica el comportamiento cuando el arreglo
        está ordenado de forma descendente.
        """
        arr = [5, 4, 3, 2, 1]

        idx = partition(arr, 0, len(arr) - 1)

        pivot = arr[idx]

        assert all(arr[i] <= pivot for i in range(idx))


# ─────────────────────────────────────────────────────────────────────────────
# TESTS DE quickselect()
# ─────────────────────────────────────────────────────────────────────────────

class TestQuickselect:
    """
    Pruebas para el algoritmo Quickselect.

    Quickselect permite encontrar el elemento k-ésimo
    más pequeño de un arreglo sin ordenarlo completamente.
    """

    def test_finds_minimum(self):
        """
        Verifica que Quickselect encuentre
        el elemento mínimo.
        """
        arr = [7, 2, 10, 4, 1]

        result = quickselect(
            arr,
            0,
            len(arr) - 1,
            0
        )

        assert result == 1

    def test_finds_maximum(self):
        """
        Verifica que Quickselect encuentre
        el elemento máximo.
        """
        arr = [7, 2, 10, 4, 1]

        result = quickselect(
            arr,
            0,
            len(arr) - 1,
            len(arr) - 1
        )

        assert result == 10

    def test_finds_median_position(self):
        """
        Verifica que Quickselect encuentre
        correctamente el elemento central.

        Arreglo ordenado:
        [1, 2, 4, 7, 10]

        Índice 2 → valor 4
        """
        arr = [7, 2, 10, 4, 1]

        result = quickselect(
            arr,
            0,
            len(arr) - 1,
            2
        )

        assert result == 4

    def test_single_element(self):
        """
        Verifica el comportamiento para
        un arreglo de un solo elemento.
        """
        arr = [42]

        assert quickselect(arr, 0, 0, 0) == 42

    def test_two_elements_first(self):
        """
        Verifica la búsqueda del primer elemento
        en un arreglo de tamaño 2.
        """
        arr = [8, 3]

        result = quickselect(
            arr,
            0,
            1,
            0
        )

        assert result == 3

    def test_two_elements_second(self):
        """
        Verifica la búsqueda del segundo elemento
        en un arreglo de tamaño 2.
        """
        arr = [8, 3]

        result = quickselect(
            arr,
            0,
            1,
            1
        )

        assert result == 8

    def test_all_equal_elements(self):
        """
        Verifica que funcione correctamente cuando
        todos los elementos son iguales.
        """
        arr = [5, 5, 5, 5]

        assert quickselect(
            arr,
            0,
            len(arr) - 1,
            2
        ) == 5

    def test_duplicates_present(self):
        """
        Verifica el comportamiento con valores duplicados.

        Ordenado:
        [1, 1, 3, 3, 3]

        Índice 1 → valor 1
        """
        arr = [3, 1, 3, 1, 3]

        result = quickselect(
            arr,
            0,
            len(arr) - 1,
            1
        )

        assert result == 1


# ─────────────────────────────────────────────────────────────────────────────
# TESTS DE find_median()
# ─────────────────────────────────────────────────────────────────────────────

class TestFindMedian:
    """
    Pruebas para la función find_median().

    Esta función utiliza Quickselect para obtener
    la mediana de una lista sin ordenarla completamente.
    """

    def test_odd_length_unsorted(self):
        """
        Verifica la mediana de un arreglo impar desordenado.

        Ordenado:
        [1, 2, 4, 5, 7, 9, 10]

        Índice 3 → valor 5
        """
        numbers = [9, 1, 7, 2, 10, 4, 5]

        assert find_median(numbers) == 5

    def test_even_length_returns_upper_middle(self):
        """
        Verifica que para arreglos pares se utilice
        el elemento superior central.

        Ordenado:
        [1, 2, 3, 4]

        Índice 2 → valor 3
        """
        arr = [4, 1, 3, 2]

        assert find_median(arr) == 3

    def test_single_element(self):
        """
        Verifica el caso de una lista con
        un único elemento.
        """
        assert find_median([99]) == 99

    def test_two_elements(self):
        """
        Verifica el cálculo de la mediana
        para una lista de tamaño 2.
        """
        assert find_median([5, 1]) == 5

    def test_already_sorted_input(self):
        """
        Verifica el funcionamiento con una lista
        previamente ordenada.
        """
        arr = [1, 2, 3, 4, 5]

        assert find_median(arr) == 3

    def test_reverse_sorted_input(self):
        """
        Verifica el funcionamiento con una lista
        ordenada de forma descendente.
        """
        arr = [5, 4, 3, 2, 1]

        assert find_median(arr) == 3

    def test_does_not_mutate_original_list(self):
        """
        Verifica que find_median() no modifique
        la lista original recibida.
        """
        arr = [3, 1, 4, 1, 5, 9, 2, 6]

        original = arr.copy()

        find_median(arr)

        assert arr == original

    def test_all_equal_elements(self):
        """
        Verifica el comportamiento cuando todos
        los elementos son iguales.
        """
        arr = [7, 7, 7, 7, 7]

        assert find_median(arr) == 7

    def test_with_negative_numbers(self):
        """
        Verifica el cálculo de la mediana
        con números negativos.

        Ordenado:
        [-5, -4, -3, -1, -1]

        Índice 2 → valor -3
        """
        arr = [-3, -1, -4, -1, -5]

        assert find_median(arr) == -3

    def test_large_list_correctness(self):
        """
        Verifica la exactitud de la mediana
        utilizando una lista grande de números aleatorios.
        """
        import random

        random.seed(0)

        arr = random.sample(range(1000), 101)

        result = find_median(arr)

        expected = sorted(arr)[101 // 2]

        assert result == expected
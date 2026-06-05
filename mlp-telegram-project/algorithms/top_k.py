"""
top_k.py
--------

Implementación de dos estrategias para obtener los k elementos más grandes
de una colección de datos.

Este módulo permite comparar dos enfoques ampliamente utilizados en el
análisis y diseño de algoritmos:

1. Heap (Montículo)
   Utiliza una estructura de datos Heap para recuperar eficientemente
   los k elementos más grandes sin ordenar completamente la colección.

2. Ordenamiento Completo
   Ordena todos los elementos de forma descendente y posteriormente
   selecciona los primeros k elementos.

Estas implementaciones son utilizadas en el proyecto para realizar
experimentos de rendimiento y comparar complejidades algorítmicas
mediante benchmarking.

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import heapq


def top_k_heap(
    values,
    k
):
    """
    Obtiene los k elementos más grandes utilizando una estructura Heap.

    La función aprovecha la implementación interna de heapq.nlargest(),
    la cual utiliza un heap para encontrar los elementos máximos de forma
    más eficiente que ordenar completamente la colección cuando k es
    significativamente menor que n.

    Parameters
    ----------
    values : list
        Colección de valores numéricos.

    k : int
        Cantidad de elementos máximos que se desean recuperar.

    Returns
    -------
    list
        Lista con los k valores más grandes ordenados de mayor a menor.

    Example
    -------
    >>> values = [10, 5, 20, 7, 30]
    >>> top_k_heap(values, 3)

    [30, 20, 10]

    Time Complexity
    ---------------
    O(n log k)

    donde:
    - n representa la cantidad total de elementos.
    - k representa la cantidad de elementos solicitados.

    Esta complejidad resulta especialmente eficiente cuando
    k << n.

    Space Complexity
    ----------------
    O(k)

    debido a la estructura Heap utilizada internamente.
    """

    return heapq.nlargest(
        k,
        values
    )


def top_k_sort(
    values,
    k
):
    """
    Obtiene los k elementos más grandes mediante ordenamiento completo.

    La función ordena todos los elementos de forma descendente y luego
    selecciona los primeros k valores de la lista resultante.

    Aunque es una solución simple y fácil de implementar, suele ser menos
    eficiente que la estrategia basada en Heap cuando únicamente se requiere
    una pequeña cantidad de elementos máximos.

    Parameters
    ----------
    values : list
        Colección de valores numéricos.

    k : int
        Cantidad de elementos máximos que se desean recuperar.

    Returns
    -------
    list
        Lista con los k valores más grandes ordenados de mayor a menor.

    Example
    -------
    >>> values = [10, 5, 20, 7, 30]
    >>> top_k_sort(values, 3)

    [30, 20, 10]

    Time Complexity
    ---------------
    O(n log n)

    debido al proceso completo de ordenamiento.

    Space Complexity
    ----------------
    O(n)

    debido a la creación de una nueva lista ordenada.

    Notes
    -----
    Este enfoque resulta adecuado cuando:
    - Se requiere el conjunto completamente ordenado.
    - El valor de k es cercano a n.

    Para valores pequeños de k, la estrategia basada en Heap suele
    presentar un mejor rendimiento.
    """

    sorted_values = sorted(
        values,
        reverse=True
    )

    return sorted_values[:k]
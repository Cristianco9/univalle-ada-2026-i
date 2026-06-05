"""
quickselect.py
--------------

Implementación del algoritmo Quickselect para la selección eficiente
de elementos de orden estadístico dentro de una colección de datos.

Quickselect es una variante del algoritmo Quicksort que permite encontrar
el k-ésimo elemento más pequeño de una lista sin necesidad de ordenar
completamente la estructura de datos.

En este proyecto se utiliza para calcular la mediana de conjuntos de datos
empleados durante el análisis y procesamiento de información relacionada
con el entrenamiento de la red neuronal.

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""


def partition(
    arr,
    low,
    high
):
    """
    Reorganiza una porción del arreglo utilizando la estrategia de partición
    de Lomuto.

    Selecciona el último elemento como pivote y redistribuye los elementos
    de manera que:

    - Los elementos menores o iguales al pivote queden a su izquierda.
    - Los elementos mayores al pivote queden a su derecha.

    Parameters
    ----------
    arr : list
        Arreglo sobre el cual se realizará la partición.

    low : int
        Índice inicial del segmento a procesar.

    high : int
        Índice final del segmento a procesar.
        El elemento ubicado en esta posición será utilizado como pivote.

    Returns
    -------
    int
        Posición final del pivote después de la partición.

    Time Complexity
    ---------------
    O(n)

    donde n corresponde al tamaño del segmento analizado.

    Space Complexity
    ----------------
    O(1)

    ya que la partición se realiza in-place sin estructuras auxiliares.
    """

    pivot = arr[high]

    i = low

    for j in range(
        low,
        high
    ):

        if arr[j] <= pivot:

            arr[i], arr[j] = (
                arr[j],
                arr[i]
            )

            i += 1

    arr[i], arr[high] = (
        arr[high],
        arr[i]
    )

    return i


def quickselect(
    arr,
    low,
    high,
    k
):
    """
    Encuentra el elemento que ocuparía la posición k si el arreglo
    estuviera ordenado.

    El algoritmo utiliza la estrategia Divide y Vencerás, particionando
    repetidamente el arreglo y descartando la mitad que no contiene el
    elemento buscado.

    A diferencia de Quicksort, Quickselect únicamente explora la partición
    relevante, reduciendo significativamente el trabajo realizado.

    Parameters
    ----------
    arr : list
        Arreglo de elementos.

    low : int
        Índice inicial del segmento de búsqueda.

    high : int
        Índice final del segmento de búsqueda.

    k : int
        Posición objetivo dentro del arreglo ordenado.

    Returns
    -------
    any
        Elemento ubicado en la posición k.

    Example
    -------
    >>> values = [7, 2, 10, 4, 1]
    >>> quickselect(values, 0, len(values)-1, 2)

    4

    Time Complexity
    ---------------
    Caso promedio:
        O(n)

    Peor caso:
        O(n²)

    El peor caso ocurre cuando las particiones son altamente desbalanceadas.

    Space Complexity
    ----------------
    O(log n)

    debido a las llamadas recursivas.
    """

    if low == high:
        return arr[low]

    pivot_index = (
        partition(
            arr,
            low,
            high
        )
    )

    if pivot_index == k:
        return arr[k]

    elif pivot_index > k:

        return quickselect(
            arr,
            low,
            pivot_index - 1,
            k
        )

    else:

        return quickselect(
            arr,
            pivot_index + 1,
            high,
            k
        )


def find_median(
    arr
):
    """
    Calcula la mediana de una colección de datos utilizando Quickselect.

    La función crea una copia del arreglo original para evitar modificar
    los datos proporcionados por el usuario y posteriormente encuentra
    el elemento central mediante selección parcial.

    Esta estrategia es más eficiente que ordenar completamente el arreglo
    cuando únicamente se requiere la mediana.

    Parameters
    ----------
    arr : list
        Colección de valores numéricos.

    Returns
    -------
    int | float
        Valor correspondiente a la mediana del conjunto de datos.

    Example
    -------
    >>> numbers = [9, 1, 7, 2, 10, 4, 5]
    >>> find_median(numbers)

    5

    Time Complexity
    ---------------
    Caso promedio:
        O(n)

    Peor caso:
        O(n²)

    Space Complexity
    ----------------
    O(n)

    debido a la copia realizada del arreglo original.
    """

    copied = arr.copy()

    n = len(copied)

    median_index = n // 2

    return quickselect(
        copied,
        0,
        n - 1,
        median_index
    )
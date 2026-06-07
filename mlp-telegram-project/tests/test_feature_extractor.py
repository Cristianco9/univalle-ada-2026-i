"""
Pruebas unitarias para el módulo feature_extractor.py

Estas pruebas verifican:

- Extracción de features
- Detección de bucles
- Recursividad
- Ordenamiento
- Búsqueda binaria
- División por 2
- Accesos indexados
- Manejo de errores sintácticos

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

import numpy as np

from complexity.feature_extractor import (
    extract_features,
    FEATURE_SIZE
)


# ==========================================================
# CASO BASE
# ==========================================================

def test_returns_correct_feature_size():
    """
    Debe retornar exactamente 12 features.
    """

    code = """
def constant():
    return 1
"""

    features = extract_features(code)

    assert len(features) == FEATURE_SIZE


# ==========================================================
# FOR
# ==========================================================

def test_detect_for_loop():
    """
    Debe detectar al menos un bucle for.
    """

    code = """
for i in range(10):
    print(i)
"""

    features = extract_features(code)

    # índice 0 = for_loops
    assert features[0] > 0


# ==========================================================
# WHILE
# ==========================================================

def test_detect_while_loop():
    """
    Debe detectar bucles while.
    """

    code = """
n = 10

while n > 0:
    n -= 1
"""

    features = extract_features(code)

    # índice 1 = while_loops
    assert features[1] > 0


# ==========================================================
# ANIDAMIENTO
# ==========================================================

def test_detect_nested_loops():
    """
    Debe registrar profundidad de anidamiento.
    """

    code = """
for i in range(10):
    for j in range(10):
        pass
"""

    features = extract_features(code)

    # índice 2 = max_depth
    assert features[2] > 0


# ==========================================================
# RECURSIVIDAD
# ==========================================================

def test_detect_recursion():
    """
    Debe detectar llamadas recursivas.
    """

    code = """
def factorial(n):

    if n <= 1:
        return 1

    return n * factorial(n - 1)
"""

    features = extract_features(code)

    # índice 3 = has_recursion
    # índice 4 = recursive_calls
    assert features[3] > 0
    assert features[4] > 0


# ==========================================================
# SORT
# ==========================================================

def test_detect_sorted_call():
    """
    Debe detectar uso de sorted().
    """

    code = """
def ordenar(arr):
    return sorted(arr)
"""

    features = extract_features(code)

    # índice 5 = has_sort
    assert features[5] > 0


# ==========================================================
# BÚSQUEDA BINARIA
# ==========================================================

def test_detect_binary_search_pattern():
    """
    Debe detectar patrón heurístico de búsqueda binaria.
    """

    code = """
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
"""

    features = extract_features(code)

    # índice 6 = has_binary_search
    assert features[6] > 0


# ==========================================================
# LLAMADAS A FUNCIONES
# ==========================================================

def test_detect_function_calls():
    """
    Debe contar llamadas a funciones.
    """

    code = """
print("hola")
len([1,2,3])
"""

    features = extract_features(code)

    # índice 7 = total_calls
    assert features[7] > 0


# ==========================================================
# DIVISIÓN ENTRE DOS
# ==========================================================

def test_detect_divide_by_two():
    """
    Debe detectar el patrón // 2.
    """

    code = """
mid = n // 2
"""

    features = extract_features(code)

    # índice 9 = has_divide_by_2
    assert features[9] > 0


# ==========================================================
# ACCESO INDEXADO
# ==========================================================

def test_detect_hash_or_index_access():
    """
    Debe detectar arr[i] o dict[key].
    """

    code = """
value = arr[0]
"""

    features = extract_features(code)

    # índice 11 = has_hash_access
    assert features[11] > 0


# ==========================================================
# ERROR SINTÁCTICO
# ==========================================================

def test_invalid_python_returns_zeros():
    """
    Si el código tiene errores sintácticos,
    debe devolver un vector de ceros.
    """

    code = """
def broken(
"""

    features = extract_features(code)

    assert np.array_equal(
        features,
        np.zeros(FEATURE_SIZE)
    )


# ==========================================================
# NORMALIZACIÓN
# ==========================================================

def test_features_are_normalized():
    """
    Todas las features deben estar en [0,1].
    """

    code = """
for i in range(100):
    for j in range(100):
        print(i, j)
"""

    features = extract_features(code)

    assert np.all(features >= 0)
    assert np.all(features <= 1)
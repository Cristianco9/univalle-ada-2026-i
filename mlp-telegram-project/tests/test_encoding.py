"""
Pruebas unitarias para encoding.py

Se valida:

- One-Hot Encoding básico
- Una sola etiqueta
- Todas las clases
- Salida con dimensiones correctas
- Una única activación por fila
- Entrada como lista
- Entrada como numpy array
- Etiquetas repetidas

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

import numpy as np

from utils.encoding import one_hot_encode


# ==========================================================
# CASO BÁSICO
# ==========================================================

def test_one_hot_basic():
    """
    Debe generar correctamente la matriz One-Hot.
    """

    y = [0, 2, 1]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    expected = np.array([
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ])

    assert np.array_equal(
        result,
        expected
    )


# ==========================================================
# UNA SOLA ETIQUETA
# ==========================================================

def test_single_label():
    """
    Debe funcionar con una única muestra.
    """

    y = [1]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    expected = np.array([
        [0, 1, 0]
    ])

    assert np.array_equal(
        result,
        expected
    )


# ==========================================================
# TODAS LAS CLASES
# ==========================================================

def test_all_classes_present():
    """
    Debe representar correctamente todas las clases.
    """

    y = [0, 1, 2, 3]

    result = one_hot_encode(
        y,
        num_classes=4
    )

    assert result.shape == (4, 4)

    assert np.array_equal(
        result[0],
        [1, 0, 0, 0]
    )

    assert np.array_equal(
        result[3],
        [0, 0, 0, 1]
    )


# ==========================================================
# DIMENSIONES CORRECTAS
# ==========================================================

def test_output_shape():
    """
    La matriz debe tener dimensiones
    (n_muestras, n_clases).
    """

    y = [0, 1, 2, 1, 0]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    assert result.shape == (5, 3)


# ==========================================================
# UNA ACTIVACIÓN POR FILA
# ==========================================================

def test_one_active_value_per_row():
    """
    Cada fila debe contener exactamente un 1.
    """

    y = [0, 1, 2, 1]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    for row in result:

        assert row.sum() == 1


# ==========================================================
# ENTRADA COMO LISTA
# ==========================================================

def test_accepts_python_list():
    """
    Debe aceptar listas de Python.
    """

    y = [0, 2]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    assert result.shape == (2, 3)


# ==========================================================
# ENTRADA COMO NUMPY ARRAY
# ==========================================================

def test_accepts_numpy_array():
    """
    Debe aceptar arreglos de NumPy.
    """

    y = np.array([
        0,
        1,
        2
    ])

    result = one_hot_encode(
        y,
        num_classes=3
    )

    assert result.shape == (3, 3)


# ==========================================================
# ETIQUETAS REPETIDAS
# ==========================================================

def test_repeated_labels():
    """
    Debe codificar correctamente
    etiquetas repetidas.
    """

    y = [2, 2, 2]

    result = one_hot_encode(
        y,
        num_classes=3
    )

    expected = np.array([
        [0, 0, 1],
        [0, 0, 1],
        [0, 0, 1]
    ])

    assert np.array_equal(
        result,
        expected
    )


# ==========================================================
# PRIMERA CLASE
# ==========================================================

def test_first_class_encoding():
    """
    Debe activar la primera posición
    para la clase 0.
    """

    result = one_hot_encode(
        [0],
        num_classes=4
    )

    assert np.array_equal(
        result[0],
        [1, 0, 0, 0]
    )


# ==========================================================
# ÚLTIMA CLASE
# ==========================================================

def test_last_class_encoding():
    """
    Debe activar la última posición
    para la última clase.
    """

    result = one_hot_encode(
        [3],
        num_classes=4
    )

    assert np.array_equal(
        result[0],
        [0, 0, 0, 1]
    )
"""
Pruebas unitarias para complexity_model_service.py

Se valida:

- Función ReLU
- Función Softmax
- Gradient Clipping
- Conservación de dimensiones
- Suma de probabilidades
- Casos límite

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

import numpy as np

from mlp.complexity_model_service import (
    relu,
    softmax,
    clip_grad
)


# ==========================================================
# RELU
# ==========================================================

def test_relu_negative_values():
    """
    Los valores negativos deben convertirse en cero.
    """

    x = np.array([
        -5,
        -1,
        -0.5
    ])

    result = relu(x)

    expected = np.array([
        0,
        0,
        0
    ])

    assert np.array_equal(
        result,
        expected
    )


def test_relu_positive_values():
    """
    Los valores positivos deben mantenerse.
    """

    x = np.array([
        1,
        2,
        3
    ])

    result = relu(x)

    assert np.array_equal(
        result,
        x
    )


def test_relu_mixed_values():
    """
    Debe transformar únicamente
    los valores negativos.
    """

    x = np.array([
        -2,
        0,
        5
    ])

    result = relu(x)

    expected = np.array([
        0,
        0,
        5
    ])

    assert np.array_equal(
        result,
        expected
    )


# ==========================================================
# SOFTMAX
# ==========================================================

def test_softmax_probabilities_sum_to_one():
    """
    La suma de probabilidades debe ser 1.
    """

    x = np.array([
        1,
        2,
        3
    ])

    result = softmax(x)

    assert np.isclose(
        result.sum(),
        1.0
    )


def test_softmax_output_shape():
    """
    Softmax debe conservar
    la dimensión del vector.
    """

    x = np.array([
        1,
        2,
        3,
        4
    ])

    result = softmax(x)

    assert result.shape == x.shape


def test_softmax_positive_outputs():
    """
    Todas las probabilidades
    deben ser positivas.
    """

    x = np.array([
        1,
        2,
        3
    ])

    result = softmax(x)

    assert np.all(result > 0)


def test_softmax_equal_inputs():
    """
    Si todas las entradas son iguales,
    las probabilidades deben ser uniformes.
    """

    x = np.array([
        5,
        5,
        5
    ])

    result = softmax(x)

    expected = np.array([
        1/3,
        1/3,
        1/3
    ])

    assert np.allclose(
        result,
        expected
    )


def test_softmax_highest_value_has_highest_probability():
    """
    El valor más grande debe producir
    la mayor probabilidad.
    """

    x = np.array([
        1,
        10,
        2
    ])

    result = softmax(x)

    assert np.argmax(result) == 1


# ==========================================================
# CLIP GRADIENT
# ==========================================================

def test_clip_grad_large_vector():
    """
    Debe reducir gradientes cuya norma
    supera el valor de clipping.
    """

    g = np.array([
        100.0,
        100.0
    ])

    clipped = clip_grad(
        g,
        clip=1.0
    )

    norm = np.linalg.norm(
        clipped
    )

    assert norm <= 1.0 + 1e-6


def test_clip_grad_small_vector():
    """
    No debe modificar gradientes
    dentro del límite permitido.
    """

    g = np.array([
        0.1,
        0.2
    ])

    clipped = clip_grad(
        g,
        clip=1.0
    )

    assert np.allclose(
        clipped,
        g
    )


def test_clip_grad_zero_vector():
    """
    Debe manejar correctamente
    vectores nulos.
    """

    g = np.array([
        0.0,
        0.0
    ])

    clipped = clip_grad(
        g,
        clip=1.0
    )

    assert np.array_equal(
        clipped,
        g
    )


# ==========================================================
# CONSERVACIÓN DE DIMENSIONES
# ==========================================================

def test_clip_grad_preserves_shape():
    """
    El clipping no debe modificar
    la forma del vector.
    """

    g = np.array([
        10,
        20,
        30,
        40
    ])

    clipped = clip_grad(
        g,
        clip=1.0
    )

    assert clipped.shape == g.shape
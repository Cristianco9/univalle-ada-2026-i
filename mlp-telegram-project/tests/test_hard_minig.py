"""
Pruebas unitarias para el módulo hard_mining.py.

Este archivo valida el correcto funcionamiento de la función
get_hard_examples(), encargada de identificar los ejemplos más
difíciles (hard examples) durante el entrenamiento de la red neuronal.

Objetivos de las pruebas:
- Verificar que se retornen los k mayores valores de pérdida (loss).
- Comprobar que se conserven los índices originales.
- Validar el comportamiento con diferentes tamaños de entrada.
- Evaluar escenarios límite (edge cases).
- Garantizar que la lista original no sea modificada.

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

# Framework utilizado para ejecutar pruebas unitarias
import pytest

# Función que será evaluada
from algorithms.hard_mining import get_hard_examples


# ──────────────────────────────────────────────────────────────────────────────
# CASOS DE PRUEBA PRINCIPALES (HAPPY PATH)
# ──────────────────────────────────────────────────────────────────────────────

class TestGetHardExamplesHappyPath:
    """
    Conjunto de pruebas para verificar el comportamiento esperado
    de la función en escenarios normales de uso.
    """

    def test_returns_k_elements(self):
        """
        Verifica que la función retorne exactamente k elementos.
        """
        losses = [0.2, 0.9, 0.1, 0.7, 0.95, 0.5]

        result = get_hard_examples(losses, k=3)

        assert len(result) == 3

    def test_correct_top3_values(self):
        """
        Verifica que los tres valores de pérdida más altos
        sean retornados correctamente.
        """
        losses = [0.2, 0.9, 0.1, 0.7, 0.95, 0.5]

        result = get_hard_examples(losses, k=3)

        loss_values = [loss for loss, _ in result]

        assert loss_values == pytest.approx([
            0.95,
            0.9,
            0.7
        ])

    def test_correct_original_indices(self):
        """
        Verifica que se conserven los índices originales
        asociados a cada pérdida.
        """
        losses = [0.2, 0.9, 0.1, 0.7, 0.95, 0.5]

        result = get_hard_examples(losses, k=3)

        # (0.95, índice=4)
        # (0.9, índice=1)
        # (0.7, índice=3)
        indices = [idx for _, idx in result]

        assert indices == [4, 1, 3]

    def test_sorted_descending_by_loss(self):
        """
        Verifica que los resultados se encuentren ordenados
        de mayor a menor pérdida.
        """
        losses = [0.3, 0.8, 0.1, 0.6, 0.9, 0.4]

        result = get_hard_examples(losses, k=4)

        loss_values = [loss for loss, _ in result]

        assert loss_values == sorted(
            loss_values,
            reverse=True
        )

    def test_default_k_is_5(self):
        """
        Verifica que el valor por defecto de k sea 5.
        """
        losses = [
            float(i) / 10
            for i in range(10)
        ]

        result = get_hard_examples(losses)

        assert len(result) == 5

    def test_k_equals_length_returns_all(self):
        """
        Si k es igual al tamaño de la lista,
        deben retornarse todos los elementos.
        """
        losses = [0.1, 0.5, 0.3]

        result = get_hard_examples(losses, k=3)

        assert len(result) == 3

    def test_single_element(self):
        """
        Verifica el comportamiento cuando existe
        un único elemento en la lista.
        """
        result = get_hard_examples(
            [0.42],
            k=1
        )

        assert result == [(0.42, 0)]

    def test_result_contains_tuples_of_loss_and_index(self):
        """
        Verifica que cada elemento retornado sea una tupla
        compuesta por:
            (loss, índice)
        """
        losses = [0.1, 0.9, 0.5]

        result = get_hard_examples(losses, k=2)

        for item in result:

            assert len(item) == 2

            loss, idx = item

            assert isinstance(loss, float)
            assert isinstance(idx, int)

    def test_indices_point_to_correct_original_positions(self):
        """
        Verifica que cada índice corresponda realmente
        a la posición original de la pérdida.
        """
        losses = [0.9, 0.1, 0.8, 0.2, 0.7]

        result = get_hard_examples(losses, k=3)

        for loss, idx in result:

            assert losses[idx] == pytest.approx(loss)


# ──────────────────────────────────────────────────────────────────────────────
# CASOS LÍMITE (EDGE CASES)
# ──────────────────────────────────────────────────────────────────────────────

class TestGetHardExamplesEdgeCases:
    """
    Pruebas orientadas a escenarios extremos o poco comunes.
    """

    def test_all_equal_losses(self):
        """
        Verifica el comportamiento cuando todas las pérdidas
        tienen exactamente el mismo valor.
        """
        losses = [
            0.5,
            0.5,
            0.5,
            0.5
        ]

        result = get_hard_examples(losses, k=2)

        assert len(result) == 2

        for loss, _ in result:
            assert loss == pytest.approx(0.5)

    def test_losses_already_sorted_ascending(self):
        """
        Verifica el funcionamiento cuando la lista
        ya se encuentra ordenada ascendentemente.
        """
        losses = [
            0.1,
            0.2,
            0.3,
            0.4,
            0.5
        ]

        result = get_hard_examples(losses, k=3)

        loss_values = [
            loss
            for loss, _ in result
        ]

        assert loss_values == pytest.approx([
            0.5,
            0.4,
            0.3
        ])

    def test_losses_already_sorted_descending(self):
        """
        Verifica el comportamiento cuando la lista
        ya está ordenada de mayor a menor.
        """
        losses = [
            0.9,
            0.7,
            0.5,
            0.3,
            0.1
        ]

        result = get_hard_examples(losses, k=2)

        assert result[0][0] == pytest.approx(0.9)
        assert result[1][0] == pytest.approx(0.7)

    def test_zero_losses(self):
        """
        Verifica el comportamiento cuando existen pérdidas
        iguales a cero.
        """
        losses = [
            0.0,
            0.0,
            0.1
        ]

        result = get_hard_examples(losses, k=1)

        assert result[0][0] == pytest.approx(0.1)
        assert result[0][1] == 2

    def test_large_k_equal_to_list_length(self):
        """
        Verifica que la función maneje correctamente
        el caso donde k coincide con el tamaño de la lista.
        """
        losses = [0.2, 0.8, 0.5]

        result = get_hard_examples(losses, k=3)

        assert len(result) == 3

    def test_does_not_mutate_original_list(self):
        """
        Verifica que la lista original no sea modificada
        durante la ejecución de la función.
        """
        losses = [0.3, 0.9, 0.1, 0.7]

        original = losses.copy()

        get_hard_examples(losses, k=2)

        assert losses == original

    def test_negative_loss_values(self):
        """
        Verifica el funcionamiento cuando las pérdidas
        son valores negativos.
        """
        losses = [
            -0.5,
            -0.1,
            -0.9
        ]

        result = get_hard_examples(losses, k=2)

        # Los mayores valores negativos son:
        # -0.1 y -0.5

        assert result[0][0] == pytest.approx(-0.1)
        assert result[1][0] == pytest.approx(-0.5)

    def test_k_equals_1_returns_single_maximum(self):
        """
        Verifica que cuando k=1 se retorne únicamente
        el valor máximo de la lista.
        """
        losses = [
            0.3,
            0.1,
            0.8,
            0.4
        ]

        result = get_hard_examples(losses, k=1)

        assert len(result) == 1

        assert result[0] == (0.8, 2)
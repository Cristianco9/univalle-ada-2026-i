"""
Pruebas unitarias para la estructura de datos HashTable.

Este módulo valida el correcto funcionamiento de la tabla hash
implementada en data_structures/hash_table.py.

Objetivos de las pruebas:
- Verificar operaciones básicas de inserción (set).
- Verificar operaciones de consulta (get).
- Validar actualización de claves existentes.
- Comprobar manejo de colisiones mediante chaining.
- Evaluar diferentes tipos de claves y valores.
- Garantizar integridad de los datos almacenados.

Autores:
    Cristian Cortes
    Katherine Arboleda

Curso:
    Análisis y Diseño de Algoritmos
    Universidad del Valle
"""

# Framework de pruebas unitarias
import pytest

# Clase que será evaluada
from data_structures.hash_table import HashTable


# ──────────────────────────────────────────────────────────────────────────────
# CASOS DE PRUEBA PRINCIPALES (HAPPY PATH)
# ──────────────────────────────────────────────────────────────────────────────

class TestHashTableHappyPath:
    """
    Pruebas para validar el funcionamiento normal
    de la tabla hash.
    """

    def test_set_and_get_string_key(self):
        """
        Verifica que una clave tipo string
        pueda almacenarse y recuperarse correctamente.
        """
        ht = HashTable()

        ht.set("name", "Alice")

        assert ht.get("name") == "Alice"

    def test_set_and_get_integer_key(self):
        """
        Verifica que una clave numérica
        pueda almacenarse y recuperarse correctamente.
        """
        ht = HashTable()

        ht.set(42, "answer")

        assert ht.get(42) == "answer"

    def test_set_and_get_multiple_keys(self):
        """
        Verifica el almacenamiento simultáneo
        de múltiples claves.
        """
        ht = HashTable()

        ht.set("a", 1)
        ht.set("b", 2)
        ht.set("c", 3)

        assert ht.get("a") == 1
        assert ht.get("b") == 2
        assert ht.get("c") == 3

    def test_update_existing_key(self):
        """
        Verifica que una clave existente
        pueda actualizar su valor.
        """
        ht = HashTable()

        ht.set("score", 10)
        ht.set("score", 99)

        assert ht.get("score") == 99

    def test_get_missing_key_returns_none(self):
        """
        Verifica que una clave inexistente
        retorne None.
        """
        ht = HashTable()

        assert ht.get("nonexistent") is None

    def test_value_can_be_none(self):
        """
        Verifica que la tabla permita
        almacenar valores None.
        """
        ht = HashTable()

        ht.set("key", None)

        assert ht.get("key") is None

    def test_value_can_be_zero(self):
        """
        Verifica que la tabla permita
        almacenar valores numéricos iguales a cero.
        """
        ht = HashTable()

        ht.set("zero", 0)

        assert ht.get("zero") == 0

    def test_value_can_be_false(self):
        """
        Verifica que se puedan almacenar
        valores booleanos.
        """
        ht = HashTable()

        ht.set("flag", False)

        assert ht.get("flag") is False

    def test_value_can_be_list(self):
        """
        Verifica que se puedan almacenar
        estructuras de datos complejas como listas.
        """
        ht = HashTable()

        ht.set("items", [1, 2, 3])

        assert ht.get("items") == [1, 2, 3]

    def test_float_value(self):
        """
        Verifica el almacenamiento de valores flotantes.
        """
        ht = HashTable()

        ht.set("loss", 0.81)

        assert ht.get("loss") == pytest.approx(0.81)

    def test_epoch_metrics_workflow(self):
        """
        Simula el almacenamiento de métricas de entrenamiento
        utilizadas por la red neuronal MLP.
        """
        ht = HashTable()

        ht.set("epoch_1_loss", 0.81)
        ht.set("epoch_2_loss", 0.54)

        assert ht.get("epoch_1_loss") == pytest.approx(0.81)
        assert ht.get("epoch_2_loss") == pytest.approx(0.54)


# ──────────────────────────────────────────────────────────────────────────────
# CASOS LÍMITE (EDGE CASES)
# ──────────────────────────────────────────────────────────────────────────────

class TestHashTableEdgeCases:
    """
    Pruebas para validar escenarios extremos,
    colisiones y condiciones especiales.
    """

    def test_custom_size_1(self):
        """
        Fuerza todas las claves al mismo bucket
        para validar el manejo de colisiones.
        """
        ht = HashTable(size=1)

        ht.set("x", 10)
        ht.set("y", 20)

        assert ht.get("x") == 10
        assert ht.get("y") == 20

    def test_update_does_not_duplicate_key(self):
        """
        Verifica que actualizar una clave existente
        no genere duplicados dentro del bucket.
        """
        ht = HashTable(size=1)

        ht.set("k", 1)
        ht.set("k", 2)
        ht.set("k", 3)

        assert ht.get("k") == 3

        bucket = ht.table[ht._hash("k")]

        keys_in_bucket = [
            pair[0]
            for pair in bucket
        ]

        assert keys_in_bucket.count("k") == 1

    def test_empty_string_key(self):
        """
        Verifica el uso de una cadena vacía
        como clave válida.
        """
        ht = HashTable()

        ht.set("", "empty")

        assert ht.get("") == "empty"

    def test_tuple_key(self):
        """
        Verifica el uso de tuplas como claves.
        """
        ht = HashTable()

        ht.set((1, 2), "tuple")

        assert ht.get((1, 2)) == "tuple"

    def test_many_keys_no_data_loss(self):
        """
        Inserta una gran cantidad de elementos
        para verificar que no exista pérdida de datos.
        """
        ht = HashTable(size=10)

        for i in range(100):
            ht.set(
                f"key_{i}",
                i * 2
            )

        for i in range(100):
            assert (
                ht.get(f"key_{i}")
                == i * 2
            )

    def test_default_size_is_100(self):
        """
        Verifica que el tamaño por defecto
        de la tabla hash sea 100 buckets.
        """
        ht = HashTable()

        assert ht.size == 100
        assert len(ht.table) == 100

    def test_hash_stays_within_bounds(self):
        """
        Verifica que la función hash
        siempre retorne índices válidos.
        """
        ht = HashTable(size=7)

        for key in [
            "a",
            "b",
            "abc",
            0,
            999,
            (1, 2)
        ]:

            idx = ht._hash(key)

            assert 0 <= idx < 7

    def test_overwrite_preserves_other_keys(self):
        """
        Verifica que actualizar una clave
        no afecte el contenido de otras claves.
        """
        ht = HashTable()

        ht.set("a", 1)
        ht.set("b", 2)

        ht.set("a", 99)

        assert ht.get("b") == 2
        assert ht.get("a") == 99
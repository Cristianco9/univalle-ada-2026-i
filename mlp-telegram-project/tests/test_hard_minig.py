"""
test_hard_mining.py
-------------------

Módulo de prueba encargado de validar el funcionamiento del algoritmo
de Hard Example Mining implementado en el proyecto.

El objetivo de esta prueba es identificar los ejemplos con mayor pérdida
(loss) dentro de un conjunto de resultados de entrenamiento, simulando
el proceso utilizado por la red neuronal para detectar los casos más
difíciles de aprender.

Hard Example Mining:
--------------------

Esta técnica consiste en seleccionar los ejemplos que generan el mayor
error durante el entrenamiento de un modelo de Machine Learning.

Estos ejemplos pueden utilizarse para:

- Analizar errores del modelo.
- Mejorar el conjunto de entrenamiento.
- Reentrenar la red con ejemplos difíciles.
- Detectar patrones problemáticos en la clasificación.

Proceso:
---------

Lista de pérdidas (losses)
            │
            ▼
    get_hard_examples()
            │
            ▼
 Selección Top-K pérdidas
            │
            ▼
 (loss, índice)
            │
            ▼
 Mostrar resultados

Tecnologías utilizadas:
-----------------------
- Python
- Heap Queue (heapq)
- Hard Example Mining

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

from algorithms.hard_mining import (
    get_hard_examples
)

# -------------------------------------------------------------------------
# Datos de prueba
# -------------------------------------------------------------------------
#
# Simulan pérdidas obtenidas durante el entrenamiento
# de una red neuronal.
#
# Mientras más alto sea el valor,
# más difícil resultó clasificar ese ejemplo.
#

losses = [
    0.2,
    0.9,
    0.1,
    0.7,
    0.95,
    0.5
]

# -------------------------------------------------------------------------
# Ejecución de Hard Example Mining
# -------------------------------------------------------------------------
#
# Selecciona los 3 ejemplos con mayor pérdida.
#
# Resultado esperado:
#
# [
#     (0.95, 4),
#     (0.9, 1),
#     (0.7, 3)
# ]
#

hard_examples = (
    get_hard_examples(
        losses,
        k=3
    )
)

# -------------------------------------------------------------------------
# Mostrar resultados
# -------------------------------------------------------------------------
#
# Imprime los ejemplos más difíciles encontrados
# durante el análisis.
#

print(
    hard_examples
)


if __name__ == "__main__":
    """
    Punto de entrada principal.

    Permite ejecutar la prueba de forma independiente
    para verificar el correcto funcionamiento del
    algoritmo Hard Example Mining.

    Resultado esperado:
    -------------------

    Los elementos devueltos deben estar ordenados
    de mayor a menor pérdida y acompañados de
    su índice original dentro de la lista.

    Time Complexity
    ---------------
    O(n log k)

    donde:

        n = cantidad de pérdidas analizadas
        k = cantidad de ejemplos difíciles solicitados

    Space Complexity
    ----------------
    O(k)
    """

    pass
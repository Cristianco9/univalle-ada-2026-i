"""
hard_mining.py
--------------

Módulo encargado de implementar la estrategia de Hard Example Mining (HEM)
utilizada durante el entrenamiento de la red neuronal multicapa (MLP).

El objetivo de esta técnica es identificar los ejemplos que generan los
mayores valores de pérdida (loss), permitiendo analizar los casos donde
el modelo presenta más dificultades para realizar predicciones correctas.

Esta información puede utilizarse para:

- Evaluar el comportamiento del modelo.
- Detectar patrones difíciles de aprender.
- Analizar errores de clasificación.
- Implementar futuras estrategias de reentrenamiento.

Autores: 
    - Cristian Cortes
    - Katherine Arboleda
    
Proyecto: Clasificador de Complejidad Algorítmica mediante MLP
"""

import heapq


def get_hard_examples(losses, k=5):
    """
    Obtiene los k ejemplos con mayor valor de pérdida.

    La función asocia cada valor de pérdida con su índice original dentro
    de la lista y utiliza un Heap Máximo para recuperar eficientemente
    los ejemplos más difíciles procesados durante el entrenamiento.

    Parameters
    ----------
    losses : list[float]
        Lista que contiene los valores de pérdida generados por el modelo.

    k : int, optional
        Cantidad de ejemplos difíciles que se desean recuperar.
        Por defecto es 5.

    Returns
    -------
    list[tuple[float, int]]
        Lista de tuplas ordenadas de mayor a menor pérdida.

        Cada tupla tiene la siguiente estructura:

        (
            loss,
            index
        )

        donde:
        - loss  : valor de pérdida del ejemplo.
        - index : posición original del ejemplo en la lista.

    Example
    -------
    >>> losses = [0.2, 0.9, 0.1, 0.7, 0.95]
    >>> get_hard_examples(losses, k=3)

    [
        (0.95, 4),
        (0.90, 1),
        (0.70, 3)
    ]

    Time Complexity
    ---------------
    O(n log k)

    donde:
    - n es el número total de pérdidas registradas.
    - k es la cantidad de ejemplos difíciles solicitados.

    Space Complexity
    ----------------
    O(n)

    debido a la estructura auxiliar utilizada para almacenar las pérdidas
    indexadas.
    """

    # Asociar cada pérdida con su índice original.
    indexed_losses = [
        (
            loss,
            index
        )
        for index,
        loss in enumerate(losses)
    ]

    # Recuperar los k valores de pérdida más altos.
    hardest = heapq.nlargest(
        k,
        indexed_losses
    )

    return hardest
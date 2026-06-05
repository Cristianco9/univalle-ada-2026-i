"""
batch_loader.py
---------------

Módulo encargado de construir mini-batches de entrenamiento
utilizando una estructura de datos tipo Queue.

Este componente forma parte del proceso de entrenamiento de la
Red Neuronal Multicapa (MLP) y permite dividir el conjunto de
datos en grupos más pequeños para ser procesados de manera
eficiente durante cada época de entrenamiento.

Objetivos:
-----------

- Dividir el dataset en mini-batches.
- Reducir el consumo de memoria.
- Facilitar el entrenamiento por lotes.
- Organizar los datos utilizando una cola FIFO.
- Mejorar la eficiencia del algoritmo de aprendizaje.

Arquitectura:
-------------

Dataset Completo
        │
        ▼
 Dividir en Lotes
        │
        ▼
 Batch 1
 Batch 2
 Batch 3
 ...
 Batch N
        │
        ▼
 Queue (FIFO)
        │
        ▼
 Entrenamiento MLP

Ventajas:
----------

- Permite procesar grandes cantidades de datos.
- Facilita la implementación de Mini-Batch Gradient Descent.
- Reduce el costo computacional por iteración.
- Mejora la estabilidad del entrenamiento.

Tecnologías utilizadas:
-----------------------
- Python
- Queue Data Structure
- Mini-Batch Learning
- Machine Learning

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

from data_structures.queue import (
    Queue
)


def create_batches(
    X,
    y,
    batch_size=16
):
    """
    Divide un conjunto de datos en mini-batches y los almacena
    dentro de una estructura Queue.

    Parameters
    ----------
    X : list | numpy.ndarray
        Conjunto de características de entrada.

    y : list | numpy.ndarray
        Etiquetas asociadas a cada muestra.

    batch_size : int, optional
        Cantidad de muestras por lote.

    Returns
    -------
    Queue

        Cola que contiene pares:

        (
            X_batch,
            y_batch
        )

    Ejemplo:
    --------

    X = [1,2,3,4,5,6]
    y = [0,1,0,1,0,1]

    batch_size = 2

    Resultado:

    Queue
    ├── ([1,2], [0,1])
    ├── ([3,4], [0,1])
    └── ([5,6], [0,1])

    Time Complexity
    ---------------
    O(n)

    donde:

        n = cantidad de muestras

    Space Complexity
    ----------------
    O(n)
    """

    # ---------------------------------------------------------------------
    # Crear cola de mini-batches
    # ---------------------------------------------------------------------
    #
    # La cola almacenará cada lote generado.
    #

    queue = Queue()

    # ---------------------------------------------------------------------
    # Recorrer el dataset por bloques
    # ---------------------------------------------------------------------
    #
    # Se avanza en pasos de tamaño batch_size.
    #

    for i in range(
        0,
        len(X),
        batch_size
    ):

        # -------------------------------------------------------------
        # Extraer subconjunto de características
        # -------------------------------------------------------------

        X_batch = X[
            i:i + batch_size
        ]

        # -------------------------------------------------------------
        # Extraer subconjunto de etiquetas
        # -------------------------------------------------------------

        y_batch = y[
            i:i + batch_size
        ]

        # -------------------------------------------------------------
        # Insertar lote en la cola
        # -------------------------------------------------------------
        #
        # Cada elemento de la cola contiene:
        #
        # (
        #     X_batch,
        #     y_batch
        # )
        #

        queue.enqueue(
            (
                X_batch,
                y_batch
            )
        )

    # ---------------------------------------------------------------------
    # Retornar cola de lotes
    # ---------------------------------------------------------------------

    return queue


if __name__ == "__main__":
    """
    Prueba básica del generador de mini-batches.

    Ejemplo de uso:

        X = [1, 2, 3, 4, 5, 6]
        y = [0, 1, 0, 1, 0, 1]

        queue = create_batches(
            X,
            y,
            batch_size=2
        )

    Resultado esperado:

        Batch 1:
            X=[1,2]
            y=[0,1]

        Batch 2:
            X=[3,4]
            y=[0,1]

        Batch 3:
            X=[5,6]
            y=[0,1]

    Aplicación en el proyecto:
    --------------------------

    Este módulo es utilizado durante el entrenamiento del MLP
    para alimentar la red neuronal mediante Mini-Batch Gradient
    Descent, mejorando la eficiencia computacional y la
    convergencia del aprendizaje.
    """

    pass
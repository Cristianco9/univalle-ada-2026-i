"""
encoding.py
-----------

Módulo encargado de realizar la codificación One-Hot Encoding sobre
las etiquetas utilizadas durante el entrenamiento de la Red Neuronal
Multicapa (MLP).

La codificación One-Hot transforma etiquetas categóricas representadas
como números enteros en vectores binarios, permitiendo que la red neuronal
trabaje correctamente con problemas de clasificación multiclase.

Ejemplo:
---------

Etiquetas originales:

    [0, 2, 1]

Número de clases:

    3

Resultado:

[
    [1, 0, 0],
    [0, 0, 1],
    [0, 1, 0]
]

Cada fila representa una clase y contiene un único valor 1 que indica
la categoría correspondiente.

Arquitectura:
-------------

Etiquetas Numéricas
        │
        ▼
 One-Hot Encoder
        │
        ▼
 Matriz Binaria
        │
        ▼
 Entrenamiento MLP

Aplicación en el proyecto:
--------------------------

La salida de este módulo es utilizada durante el entrenamiento
del modelo neuronal para:

- Calcular la función de pérdida.
- Comparar predicciones contra valores reales.
- Ejecutar Backpropagation.
- Realizar clasificación multiclase.

Tecnologías utilizadas:
-----------------------
- Python
- NumPy
- Machine Learning
- Data Preprocessing

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import numpy as np


def one_hot_encode(
    y,
    num_classes
):
    """
    Convierte un conjunto de etiquetas numéricas en una representación
    One-Hot Encoding.

    Parameters
    ----------
    y : numpy.ndarray | list

        Vector de etiquetas.

        Ejemplo:

        [0, 2, 1]

    num_classes : int

        Número total de clases posibles.

    Returns
    -------
    numpy.ndarray

        Matriz codificada utilizando One-Hot Encoding.

        Ejemplo:

        [
            [1, 0, 0],
            [0, 0, 1],
            [0, 1, 0]
        ]

    Funcionamiento:
    ----------------

    Clase 0 → [1,0,0,...]

    Clase 1 → [0,1,0,...]

    Clase 2 → [0,0,1,...]

    ...

    Clase n → [0,0,0,...,1]

    Time Complexity
    ---------------
    O(n)

    donde:

        n = cantidad de etiquetas

    Space Complexity
    ----------------
    O(n * c)

    donde:

        n = cantidad de muestras
        c = número de clases
    """

    # ---------------------------------------------------------------------
    # Crear matriz de ceros
    # ---------------------------------------------------------------------
    #
    # Se genera una matriz de dimensiones:
    #
    # (cantidad_de_muestras, número_de_clases)
    #
    # Inicialmente todos los valores son 0.
    #

    encoded = np.zeros(
        (
            len(y),
            num_classes
        )
    )

    # ---------------------------------------------------------------------
    # Aplicar One-Hot Encoding
    # ---------------------------------------------------------------------
    #
    # Para cada muestra:
    #
    # encoded[fila][clase] = 1
    #
    # Ejemplo:
    #
    # y = [0,2,1]
    #
    # Resultado:
    #
    # [
    #   [1,0,0],
    #   [0,0,1],
    #   [0,1,0]
    # ]
    #

    encoded[
        np.arange(len(y)),
        y
    ] = 1

    # ---------------------------------------------------------------------
    # Retornar matriz codificada
    # ---------------------------------------------------------------------

    return encoded


if __name__ == "__main__":
    """
    Prueba básica del codificador One-Hot.

    Ejemplo:

        y = [0, 2, 1]
        num_classes = 3

    Resultado esperado:

        [
            [1,0,0],
            [0,0,1],
            [0,1,0]
        ]

    Aplicación práctica:
    --------------------

    Este procedimiento es fundamental para el entrenamiento
    de redes neuronales de clasificación, ya que permite
    representar correctamente las clases objetivo durante
    el cálculo de la pérdida y la propagación hacia atrás.
    """

    y = np.array([
        0,
        2,
        1
    ])

    result = one_hot_encode(
        y,
        num_classes=3
    )

    print("One-Hot Encoding:")
    print(result)
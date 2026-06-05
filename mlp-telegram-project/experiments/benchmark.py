"""
benchmark.py
------------

Módulo encargado de realizar pruebas experimentales de rendimiento
(Benchmarking) sobre los algoritmos Top-K implementados en el proyecto.

El objetivo principal de este componente es comparar empíricamente
el comportamiento temporal de dos estrategias diferentes para obtener
los K elementos más grandes de una colección de datos:

1. Heap-Based Top-K
2. Sort-Based Top-K

Los resultados obtenidos permiten validar experimentalmente los análisis
teóricos de complejidad estudiados durante el desarrollo del proyecto.

Comparación teórica:
--------------------

Top-K mediante Heap:
    O(n log k)

Top-K mediante Ordenamiento:
    O(n log n)

Cuando k es significativamente menor que n, la solución basada en Heap
suele presentar un mejor rendimiento.

Proceso experimental:
---------------------

Generación Aleatoria
        │
        ▼
   Dataset de Tamaño N
        │
        ├──────────────► Heap Top-K
        │                     │
        │                     ▼
        │              Tiempo Heap
        │
        └──────────────► Sort Top-K
                              │
                              ▼
                       Tiempo Sort
                              │
                              ▼
                       Comparación

Tamaños evaluados:
------------------
- 1,000 elementos
- 5,000 elementos
- 10,000 elementos
- 50,000 elementos
- 100,000 elementos

Tecnologías utilizadas:
-----------------------
- Python
- Time Performance Analysis
- Heap Algorithms
- Sorting Algorithms

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import random
import time

from algorithms.top_k import (
    top_k_heap,
    top_k_sort
)


def benchmark_top_k():
    """
    Ejecuta un benchmark comparativo entre las implementaciones
    Heap Top-K y Sort Top-K.

    Para cada tamaño de entrada se genera un conjunto de datos
    aleatorio y se mide el tiempo requerido por ambos algoritmos.

    Returns
    -------
    list[dict]

        Lista de resultados experimentales.

        Ejemplo:

        [
            {
                "n": 1000,
                "heap_time": 0.00012,
                "sort_time": 0.00045
            }
        ]

    Experimental Procedure
    ----------------------
    1. Generar datos aleatorios.
    2. Ejecutar Heap Top-K.
    3. Medir tiempo de ejecución.
    4. Ejecutar Sort Top-K.
    5. Medir tiempo de ejecución.
    6. Registrar resultados.

    Time Complexity
    ---------------
    O(m * n log n)

    donde:

    m = número de tamaños evaluados
    n = tamaño de la entrada

    El costo dominante proviene de la ejecución
    del algoritmo basado en ordenamiento.

    Space Complexity
    ----------------
    O(n)

    debido al almacenamiento temporal de los datos
    generados para cada experimento.
    """

    sizes = [
        1000,
        5000,
        10000,
        50000,
        100000
    ]

    k = 10

    results = []

    for n in sizes:

        # ---------------------------------------------------------
        # Generación de datos aleatorios para el experimento
        # ---------------------------------------------------------

        data = [
            random.randint(
                1,
                100000
            )
            for _ in range(n)
        ]

        # ---------------------------------------------------------
        # Benchmark Heap Top-K
        # ---------------------------------------------------------

        start = (
            time.perf_counter()
        )

        top_k_heap(
            data,
            k
        )

        heap_time = (
            time.perf_counter()
            - start
        )

        # ---------------------------------------------------------
        # Benchmark Sort Top-K
        # ---------------------------------------------------------

        start = (
            time.perf_counter()
        )

        top_k_sort(
            data,
            k
        )

        sort_time = (
            time.perf_counter()
            - start
        )

        # ---------------------------------------------------------
        # Almacenamiento de resultados
        # ---------------------------------------------------------

        results.append({

            "n": n,

            "heap_time":
            heap_time,

            "sort_time":
            sort_time
        })

    return results


if __name__ == "__main__":
    """
    Punto de entrada para ejecutar el benchmark
    de forma independiente.

    Muestra los resultados obtenidos para cada
    tamaño de entrada analizado.
    """

    results = (
        benchmark_top_k()
    )

    print(
        "\nBenchmark Heap vs Sort (Top-K)\n"
    )

    for result in results:

        print(
            f"N={result['n']} | "
            f"Heap={result['heap_time']:.6f}s | "
            f"Sort={result['sort_time']:.6f}s"
        )

    print(
        "\nInterpretación:"
    )

    print(
        "Heap Top-K posee complejidad O(n log k), "
        "mientras que Sort Top-K posee complejidad "
        "O(n log n)."
    )

    print(
        "Cuando k es pequeño respecto a n, "
        "Heap suele ser significativamente más eficiente."
    )
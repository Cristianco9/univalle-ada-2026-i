"""
benchmark_visualization.py
--------------------------

Módulo encargado de generar una representación gráfica de los resultados
obtenidos durante el benchmark comparativo entre los algoritmos
Heap Top-K y Sort Top-K.

La visualización permite analizar de manera experimental el crecimiento
del tiempo de ejecución a medida que aumenta el tamaño de entrada,
facilitando la validación de los análisis teóricos de complejidad.

Complejidades teóricas comparadas:
----------------------------------

Heap Top-K:
    O(n log k)

Sort Top-K:
    O(n log n)

Cuando k es mucho más pequeño que n, la implementación basada
en Heap suele ser más eficiente.

Arquitectura:
-------------

Benchmark Module
        │
        ▼
 Resultados Experimentales
        │
        ▼
 Procesamiento de Datos
        │
        ▼
     Matplotlib
        │
        ▼
 Visualización Comparativa

Tecnologías utilizadas:
-----------------------
- Python
- Matplotlib
- Data Visualization
- Algorithm Analysis

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import matplotlib.pyplot as plt

from experiments.benchmark import (
    benchmark_top_k
)

# -------------------------------------------------------------------------
# Ejecutar benchmark
# -------------------------------------------------------------------------
#
# Obtiene los resultados experimentales para distintos tamaños
# de entrada utilizando ambas implementaciones Top-K.
#
# Estructura esperada:
#
# [
#     {
#         "n": 1000,
#         "heap_time": 0.00012,
#         "sort_time": 0.00054
#     },
#     ...
# ]
#

results = benchmark_top_k()

# -------------------------------------------------------------------------
# Extraer tamaños de entrada
# -------------------------------------------------------------------------
#
# Estos valores serán utilizados como eje X de la gráfica.
#

sizes = [
    r["n"]
    for r in results
]

# -------------------------------------------------------------------------
# Extraer tiempos Heap Top-K
# -------------------------------------------------------------------------
#
# Serie correspondiente al algoritmo basado en Heap.
#

heap_times = [
    r["heap_time"]
    for r in results
]

# -------------------------------------------------------------------------
# Extraer tiempos Sort Top-K
# -------------------------------------------------------------------------
#
# Serie correspondiente al algoritmo basado en ordenamiento.
#

sort_times = [
    r["sort_time"]
    for r in results
]

# -------------------------------------------------------------------------
# Crear figura
# -------------------------------------------------------------------------
#
# Se crea una ventana gráfica de 10x5 pulgadas para mejorar
# la legibilidad de los resultados.
#

plt.figure(
    figsize=(10, 5)
)

# -------------------------------------------------------------------------
# Graficar Heap Top-K
# -------------------------------------------------------------------------
#
# Representa los tiempos obtenidos utilizando heapq.
#
# Complejidad teórica:
# O(n log k)
#

plt.plot(
    sizes,
    heap_times,
    label="Heap Top-K"
)

# -------------------------------------------------------------------------
# Graficar Sort Top-K
# -------------------------------------------------------------------------
#
# Representa los tiempos obtenidos utilizando ordenamiento completo.
#
# Complejidad teórica:
# O(n log n)
#

plt.plot(
    sizes,
    sort_times,
    label="Sort Top-K"
)

# -------------------------------------------------------------------------
# Etiqueta eje X
# -------------------------------------------------------------------------
#
# Tamaño de entrada utilizado en cada experimento.
#

plt.xlabel(
    "Input Size (n)"
)

# -------------------------------------------------------------------------
# Etiqueta eje Y
# -------------------------------------------------------------------------
#
# Tiempo de ejecución medido en segundos.
#

plt.ylabel(
    "Execution Time (seconds)"
)

# -------------------------------------------------------------------------
# Título principal
# -------------------------------------------------------------------------
#
# Describe la comparación realizada.
#

plt.title(
    "Heap vs Sort Top-K"
)

# -------------------------------------------------------------------------
# Mostrar leyenda
# -------------------------------------------------------------------------
#
# Permite identificar cada curva de la gráfica.
#

plt.legend()

# -------------------------------------------------------------------------
# Mostrar cuadrícula
# -------------------------------------------------------------------------
#
# Facilita la lectura de valores y comparación visual.
#

plt.grid(True)

# -------------------------------------------------------------------------
# Renderizar gráfica
# -------------------------------------------------------------------------
#
# Muestra la visualización final al usuario.
#

plt.show()


if __name__ == "__main__":
    """
    Punto de entrada principal.

    Al ejecutar este archivo se generará una gráfica comparativa
    entre Heap Top-K y Sort Top-K utilizando los resultados
    producidos por el benchmark experimental.

    Interpretación esperada:
    ------------------------

    - Heap Top-K debería presentar mejor escalabilidad.
    - Sort Top-K crece más rápidamente conforme aumenta n.
    - La diferencia se hace más evidente para conjuntos
      de datos grandes.

    Time Complexity
    ---------------
    O(m)

    donde m corresponde al número de resultados
    generados por el benchmark.

    Space Complexity
    ----------------
    O(m)
    """

    pass
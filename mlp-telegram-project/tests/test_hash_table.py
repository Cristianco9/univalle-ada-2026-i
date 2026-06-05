"""
test_hash_table.py
------------------

Módulo de prueba encargado de validar el funcionamiento de la estructura
de datos Hash Table implementada en el proyecto.

El objetivo de esta prueba es comprobar que los métodos de inserción
(set) y recuperación (get) funcionan correctamente para almacenar y
consultar información asociada a claves únicas.

En el contexto del proyecto, la Hash Table es utilizada para almacenar
métricas de entrenamiento del modelo neuronal, como:

- Accuracy por época.
- Loss por época.
- Estadísticas de entrenamiento.
- Resultados experimentales.

Proceso:
---------

Crear Hash Table
        │
        ▼
 Insertar Métricas
        │
        ▼
 Almacenar (clave, valor)
        │
        ▼
 Recuperar Valores
        │
        ▼
 Mostrar Resultados

Ejemplo:
---------

"epoch_1_loss" → 0.81
"epoch_2_loss" → 0.54

Tecnologías utilizadas:
-----------------------
- Python
- Hash Tables
- Data Structures

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

from data_structures.hash_table import (
    HashTable
)

# -------------------------------------------------------------------------
# Creación de la tabla hash
# -------------------------------------------------------------------------
#
# Inicializa una nueva instancia de HashTable que será utilizada
# para almacenar métricas del entrenamiento.
#

metrics = (
    HashTable()
)

# -------------------------------------------------------------------------
# Registro de métricas
# -------------------------------------------------------------------------
#
# Se almacenan pérdidas (loss) simuladas correspondientes
# a distintas épocas del entrenamiento.
#

metrics.set(
    "epoch_1_loss",
    0.81
)

metrics.set(
    "epoch_2_loss",
    0.54
)

# -------------------------------------------------------------------------
# Recuperación de métricas
# -------------------------------------------------------------------------
#
# Obtiene los valores previamente almacenados mediante
# la clave correspondiente.
#

print(
    metrics.get(
        "epoch_1_loss"
    )
)

print(
    metrics.get(
        "epoch_2_loss"
    )
)

# -------------------------------------------------------------------------
# Punto de entrada principal
# -------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Ejecuta la prueba de manera independiente.

    Resultado esperado:
    -------------------

    0.81
    0.54

    Esto confirma que:

    - La inserción mediante set() funciona correctamente.
    - La recuperación mediante get() funciona correctamente.
    - La estructura Hash Table puede utilizarse para almacenar
      métricas del modelo neuronal.

    Complejidad Temporal:
    ---------------------

    set():
        O(1) promedio

    get():
        O(1) promedio

    Complejidad Espacial:
    ---------------------

    O(n)

    donde n corresponde al número de elementos almacenados
    en la tabla hash.
    """

    pass
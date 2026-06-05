"""
test_queue.py
-------------

Módulo de prueba encargado de validar el funcionamiento de la estructura
de datos Queue (Cola) implementada en el proyecto.

El objetivo de esta prueba es verificar que la cola respete el principio
FIFO (First In, First Out), donde el primer elemento en ingresar es el
primer elemento en salir.

En el contexto del proyecto, la estructura Queue es utilizada para:

- Gestionar mini-batches durante el entrenamiento.
- Administrar secuencias de procesamiento.
- Organizar tareas en orden de llegada.
- Simular flujos de ejecución controlados.

Principio FIFO:
---------------

enqueue(10)
enqueue(20)
enqueue(30)

Estado de la cola:

FRONT → [10, 20, 30] ← REAR

dequeue()

FRONT → [20, 30] ← REAR

Proceso:
---------

Crear Cola
    │
    ▼
 Insertar Elementos
    │
    ▼
 [10, 20, 30]
    │
    ▼
 Extraer Elementos
    │
    ▼
 Verificar Orden FIFO
    │
    ▼
 Mostrar Resultados

Tecnologías utilizadas:
-----------------------
- Python
- Queue Data Structure
- FIFO Processing

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

from data_structures.queue import (
    Queue
)

# -------------------------------------------------------------------------
# Creación de la cola
# -------------------------------------------------------------------------
#
# Inicializa una nueva estructura Queue vacía.
#

queue = Queue()

# -------------------------------------------------------------------------
# Inserción de elementos
# -------------------------------------------------------------------------
#
# Los elementos se agregan al final de la cola
# utilizando la operación enqueue().
#

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# -------------------------------------------------------------------------
# Extracción del primer elemento
# -------------------------------------------------------------------------
#
# De acuerdo con el comportamiento FIFO,
# el primer elemento insertado debe ser el primero en salir.
#
# Resultado esperado:
# 10
#

print(
    queue.dequeue()
)

# -------------------------------------------------------------------------
# Extracción del segundo elemento
# -------------------------------------------------------------------------
#
# Después de eliminar el 10, el siguiente elemento
# disponible debe ser el 20.
#
# Resultado esperado:
# 20
#

print(
    queue.dequeue()
)

# -------------------------------------------------------------------------
# Consulta del tamaño actual de la cola
# -------------------------------------------------------------------------
#
# Después de eliminar dos elementos,
# únicamente debe permanecer el valor 30.
#
# Resultado esperado:
# 1
#

print(
    queue.size()
)

# -------------------------------------------------------------------------
# Punto de entrada principal
# -------------------------------------------------------------------------

if __name__ == "__main__":
    """
    Ejecuta la prueba de manera independiente.

    Resultados esperados:
    ---------------------

    10
    20
    1

    Validaciones realizadas:
    ------------------------

    ✓ Inserción mediante enqueue()
    ✓ Extracción mediante dequeue()
    ✓ Comportamiento FIFO
    ✓ Cálculo correcto del tamaño de la cola

    Complejidad Temporal:
    ---------------------

    enqueue():
        O(1)

    dequeue():
        O(n)

    size():
        O(1)

    Complejidad Espacial:
    ---------------------

    O(n)

    donde n corresponde a la cantidad de elementos
    almacenados en la cola.
    """

    pass
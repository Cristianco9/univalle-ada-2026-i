"""
app.py
------

API REST desarrollada con FastAPI para exponer los servicios del sistema
de clasificación de complejidad algorítmica basado en Redes Neuronales
Multicapa (MLP).

Este módulo actúa como la capa de comunicación entre clientes externos
(aplicación web, bot de Telegram o herramientas de prueba) y los
componentes internos encargados del entrenamiento, evaluación y análisis
de algoritmos.

Funcionalidades principales:
----------------------------
- Entrenamiento del modelo MLP.
- Predicción de complejidad algorítmica.
- Consulta del estado del sistema.
- Visualización de métricas de entrenamiento.
- Recuperación de ejemplos difíciles (Hard Mining).
- Ejecución de benchmarks de algoritmos.
- Consulta de complejidades teóricas implementadas.

Tecnologías utilizadas:
-----------------------
- FastAPI
- Pydantic
- NumPy
- Arquitectura REST

Autores:
    - Cristian Cortes
    - Katherine Arboleda

Proyecto:
    Clasificador de Complejidad Algorítmica mediante Redes Neuronales Multicapa (MLP)
"""

import sys
import os

# Permite importar módulos internos del proyecto
# independientemente del directorio de ejecución.
sys.path.insert(
    0,
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from fastapi import FastAPI
from pydantic import BaseModel

from mlp.complexity_model_service import (
    complexity_model_service
)

from experiments.benchmark import (
    benchmark_top_k
)


class CodeInput(BaseModel):
    """
    Modelo de datos utilizado para recibir código fuente desde
    peticiones HTTP.

    Attributes
    ----------
    code : str
        Fragmento de código Python que será analizado por el modelo
        de clasificación de complejidad algorítmica.
    """

    code: str


# -------------------------------------------------------------------------
# Configuración principal de la API
# -------------------------------------------------------------------------

app = FastAPI(
    title="MLP Algorithm API"
)


@app.get("/")
def root():
    """
    Endpoint raíz de verificación.

    Permite comprobar que la API se encuentra disponible y
    respondiendo correctamente.

    Returns
    -------
    dict
        Mensaje de confirmación.
    """

    return {
        "message": "API running"
    }


@app.get("/status")
def status():
    """
    Consulta el estado actual del sistema.

    Retorna información sobre:
    - Disponibilidad de la API.
    - Estado del modelo neuronal.
    - Precisión obtenida durante el entrenamiento.

    Returns
    -------
    dict
        Información general del sistema.
    """

    return {
        "status": "online",
        "mlp_model":
            "trained"
            if complexity_model_service.is_trained
            else "not_trained",

        "accuracy":
            complexity_model_service.accuracy,
    }


@app.post("/train_complexity")
def train_complexity():
    """
    Inicia el proceso de entrenamiento del modelo MLP.

    Durante este proceso se realiza:

    - Extracción de características.
    - Balanceo del dataset.
    - Forward propagation.
    - Backpropagation.
    - Early stopping.
    - Hard Example Mining.

    Returns
    -------
    dict
        Métricas finales del entrenamiento.
    """

    return (
        complexity_model_service
        .train_model()
    )


@app.post("/analize")
def analize(body: CodeInput):
    """
    Analiza un algoritmo escrito en Python y predice
    su complejidad temporal.

    El código recibido es procesado mediante un analizador
    sintáctico (AST), transformado en un vector de características
    y posteriormente clasificado por la red neuronal.

    Parameters
    ----------
    body : CodeInput
        Objeto que contiene el código fuente enviado por el usuario.

    Returns
    -------
    dict
        Complejidad predicha y nivel de confianza.
    """

    if not complexity_model_service.is_trained:

        return {
            "error":
            "Modelo no entrenado. Usa /train_complexity primero."
        }

    return (
        complexity_model_service
        .predict_complexity(body.code)
    )


@app.get("/complexity_metrics")
def complexity_metrics():
    """
    Recupera las métricas registradas durante el entrenamiento.

    Las métricas incluyen:

    - Accuracy por época.
    - Loss por época.

    Returns
    -------
    dict
        Historial completo del entrenamiento.
    """

    return (
        complexity_model_service
        .get_training_metrics()
    )


@app.get("/hard-examples")
def hard_examples():
    """
    Obtiene los ejemplos más difíciles identificados
    durante el entrenamiento del modelo.

    La selección se realiza utilizando la técnica
    Hard Example Mining.

    Returns
    -------
    dict
        Lista de ejemplos con mayor pérdida.
    """

    return {
        "hard_examples":
            complexity_model_service
            .get_hard_examples()
    }


@app.get("/benchmark")
def benchmark():
    """
    Ejecuta un benchmark comparativo entre las implementaciones
    Top-K basadas en Heap y Ordenamiento.

    El objetivo es analizar empíricamente el comportamiento
    temporal de ambos algoritmos para distintos tamaños
    de entrada.

    Returns
    -------
    dict
        Resultados del benchmark.
    """

    return {
        "benchmark":
            benchmark_top_k()
    }


@app.get("/complexity")
def complexity():
    """
    Consulta las complejidades teóricas de los algoritmos
    y estructuras de datos implementados en el proyecto.

    Esta información sirve como referencia académica para
    comparar resultados experimentales con el análisis
    teórico de complejidad.

    Returns
    -------
    dict
        Complejidades temporales de los componentes.
    """

    return {
        "top_k_heap":          "O(n log k)",
        "top_k_sort":          "O(n log n)",
        "quickselect_average": "O(n)",
        "hash_table":          "O(1)",
        "queue":               "O(1)",
        "mlp_forward":         "O(B * h * output)",
        "mlp_backprop":        "O(B * h * output)",
    }
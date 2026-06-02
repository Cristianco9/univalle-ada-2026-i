import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import (
    FastAPI
)

from mlp.model_service import (
    model_service
)

from complexity.complexity_analyzer import analyze_complexity
from pydantic import BaseModel

from pydantic import BaseModel

from mlp.complexity_model_service import complexity_model_service

from pydantic import BaseModel

class CodeInput(BaseModel):
    code: str


app = FastAPI(
    title="MLP Algorithm API"
)


@app.get("/")
def root():

    return {
        "message":
        "API running"
    }


@app.get("/status")
def status():

    return {
        "status":
        "online",

        "mlp_model":
        (
            "trained"
            if model_service.is_trained
            else
            "not_trained"
        ),

        "accuracy":
        model_service.accuracy
    }


@app.post("/train")
def train():

    result = (
        model_service
        .train_model()
    )

    return result


@app.get("/predict")
def predict(
    sepal_length: float,
    sepal_width: float,
    petal_length: float,
    petal_width: float
):

    prediction = (
        model_service.predict(
            [
                sepal_length,
                sepal_width,
                petal_length,
                petal_width
            ]
        )
    )

    return prediction

@app.get("/metrics")
def metrics():

    return (
        model_service
        .get_metrics()
    )


@app.get("/hard-examples")
def hard_examples():

    return {
        "hard_examples":
        (
            model_service
            .get_hard_examples()
        )
    }

@app.get("/benchmark")
def benchmark():

    from experiments.benchmark import (
        benchmark_top_k
    )

    return {
        "benchmark":
        benchmark_top_k()
    }


@app.get("/complexity")
def complexity():

    return {
        "top_k_heap":
        "O(n log k)",

        "top_k_sort":
        "O(n log n)",

        "quickselect_average":
        "O(n)",

        "hash_table":
        "O(1)",

        "queue":
        "O(1)"
    }

@app.post("/train_complexity")
def train_complexity():
    """
    Entrena el MLP con el dataset de snippets de código.
    Llama a esto una vez antes de usar /analize.
    En Telegram: /train_complexity
    """
    result = complexity_model_service.train_model()
    return result


@app.post("/analize")
def analize(body: CodeInput):
    """
    Recibe un snippet de código Python y retorna su complejidad
    algorítmica predicha por el MLP.

    Ejemplo:
    {
        "code": "for i in range(n):\n  for j in range(n):\n    pass"
    }
    """
    if not complexity_model_service.is_trained:
        return {
            "error": "Modelo no entrenado. Usa /train_complexity primero."
        }

    result = complexity_model_service.predict_complexity(body.code)
    return result


@app.get("/complexity_metrics")
def complexity_metrics():
    """Retorna accuracy y loss por época del entrenamiento del clasificador."""
    return complexity_model_service.get_training_metrics()
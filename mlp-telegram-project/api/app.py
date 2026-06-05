import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from pydantic import BaseModel
from mlp.complexity_model_service import complexity_model_service
from experiments.benchmark import benchmark_top_k


class CodeInput(BaseModel):
    code: str


app = FastAPI(title="MLP Algorithm API")


@app.get("/")
def root():
    return {"message": "API running"}


@app.get("/status")
def status():
    return {
        "status":    "online",
        "mlp_model": "trained" if complexity_model_service.is_trained else "not_trained",
        "accuracy":  complexity_model_service.accuracy,
    }


@app.post("/train_complexity")
def train_complexity():
    """Entrena el MLP clasificador de complejidad algorítmica."""
    return complexity_model_service.train_model()


@app.post("/analize")
def analize(body: CodeInput):
    """
    Recibe un snippet de código Python y retorna su complejidad
    algorítmica predicha por el MLP.
    """
    if not complexity_model_service.is_trained:
        return {"error": "Modelo no entrenado. Usa /train_complexity primero."}
    return complexity_model_service.predict_complexity(body.code)


@app.get("/complexity_metrics")
def complexity_metrics():
    """Retorna accuracy y loss por epoca del entrenamiento."""
    return complexity_model_service.get_training_metrics()


@app.get("/hard-examples")
def hard_examples():
    """Retorna los ejemplos mas dificiles del entrenamiento (hard mining)."""
    return {"hard_examples": complexity_model_service.get_hard_examples()}


@app.get("/benchmark")
def benchmark():
    """Benchmark heap vs sort para top-k."""
    return {"benchmark": benchmark_top_k()}


@app.get("/complexity")
def complexity():
    """Complejidades teoricas de los modulos implementados."""
    return {
        "top_k_heap":           "O(n log k)",
        "top_k_sort":           "O(n log n)",
        "quickselect_average":  "O(n)",
        "hash_table":           "O(1)",
        "queue":                "O(1)",
        "mlp_forward":          "O(B * h * output)",
        "mlp_backprop":         "O(B * h * output)",
    }
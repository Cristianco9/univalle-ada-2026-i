from fastapi import (
    FastAPI
)

from mlp.model_service import (
    model_service
)

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
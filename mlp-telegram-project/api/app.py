from fastapi import FastAPI

app = FastAPI(
    title="MLP Algorithm Analysis API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "MLP Algorithm Analysis API running"
    }


@app.get("/status")
def status():
    return {
        "status": "online",
        "api": "connected",
        "mlp_model": "not_trained"
    }
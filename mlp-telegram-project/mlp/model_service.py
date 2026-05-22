from mlp.network import (
    NeuralNetwork
)

from data.load_dataset import (
    get_iris_dataset
)

from utils.encoding import (
    one_hot_encode
)

import numpy as np


class ModelService:

    def __init__(self):

        self.model = None
        self.is_trained = False
        self.accuracy = 0

    def train_model(self):

        (
            X_train,
            X_test,
            y_train,
            y_test
        ) = get_iris_dataset()

        y_train_encoded = (
            one_hot_encode(
                y_train,
                3
            )
        )

        self.model = (
            NeuralNetwork(
                input_size=4,
                hidden_size=8,
                output_size=3,
                learning_rate=0.01
            )
        )

        self.model.train(
            X_train,
            y_train_encoded,
            epochs=100
        )

        correct = 0

        for i in range(
            len(X_test)
        ):

            prediction = (
                self.model.predict(
                    X_test[i]
                )
            )

            if (
                prediction
                == y_test[i]
            ):
                correct += 1

        self.accuracy = (
            correct
            / len(X_test)
        ) * 100

        self.is_trained = True

        return {
            "status": "trained",
            "accuracy": round(
                self.accuracy,
                2
            )
        }

    def predict(
        self,
        features
    ):

        if not self.is_trained:
            raise Exception(
                "Model not trained"
            )

        prediction = (
            self.model.predict(
                np.array(features)
            )
        )

        flower_map = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        return {
            "prediction": (
                flower_map[
                    prediction
                ]
            )
        }


model_service = (
    ModelService()
)
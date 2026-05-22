from mlp.network import (
    NeuralNetwork
)

from data.load_dataset import (
    get_iris_dataset
)

from utils.encoding import (
    one_hot_encode
)

from utils.batch_loader import (
    create_batches
)

from data_structures.hash_table import (
    HashTable
)

from algorithms.hard_mining import (
    get_hard_examples
)

import numpy as np


class ModelService:

    def __init__(self):

        self.model = None

        self.is_trained = False

        self.accuracy = 0

        self.metrics = (
            HashTable()
        )

        self.hard_examples = []

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

        batches = (
            create_batches(
                X_train,
                y_train_encoded,
                batch_size=16
            )
        )

        losses = []

        epochs = 50

        for epoch in range(
            epochs
        ):

            correct = 0

            while (
                not batches.is_empty()
            ):

                (
                    X_batch,
                    y_batch
                ) = (
                    batches.dequeue()
                )

                for i in range(
                    len(X_batch)
                ):

                    output = (
                        self.model.forward(
                            X_batch[i]
                        )
                    )

                    prediction = (
                        np.argmax(
                            output
                        )
                    )

                    real_class = (
                        np.argmax(
                            y_batch[i]
                        )
                    )

                    if (
                        prediction
                        == real_class
                    ):
                        correct += 1

                    loss = np.mean(
                        (
                            output
                            - y_batch[i]
                        ) ** 2
                    )

                    losses.append(
                        loss
                    )

            accuracy = (
                correct
                / len(X_train)
            ) * 100

            self.metrics.set(
                f"epoch_{epoch+1}",
                round(
                    accuracy,
                    2
                )
            )

            print(
                f"Epoch "
                f"{epoch+1}"
                f"/{epochs}"
                f" Accuracy: "
                f"{accuracy:.2f}%"
            )

            batches = (
                create_batches(
                    X_train,
                    y_train_encoded,
                    batch_size=16
                )
            )

        hardest = (
            get_hard_examples(
                losses,
                k=5
            )
        )

        self.hard_examples = (
            hardest
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
            "status":
            "trained",

            "accuracy":
            round(
                self.accuracy,
                2
            )
        }

    def get_metrics(
        self
    ):

        metrics = {}

        for i in range(
            1,
            51
        ):

            key = (
                f"epoch_{i}"
            )

            metrics[key] = (
                self.metrics.get(
                    key
                )
            )

        return metrics

    def get_hard_examples(
        self
    ):

        return (
            self.hard_examples
        )

    def predict(
        self,
        features
    ):

        if (
            not self.is_trained
        ):

            raise Exception(
                "Model not trained"
            )

        prediction = (
            self.model.predict(
                np.array(
                    features
                )
            )
        )

        flower_map = {
            0: "Setosa",
            1: "Versicolor",
            2: "Virginica"
        }

        return {
            "prediction":
            flower_map[
                prediction
            ]
        }


model_service = (
    ModelService()
)
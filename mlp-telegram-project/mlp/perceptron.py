import numpy as np


class Perceptron:

    def __init__(
        self,
        input_size,
        learning_rate=0.1,
        epochs=100
    ):

        self.learning_rate = (
            learning_rate
        )

        self.epochs = epochs

        self.weights = (
            np.random.randn(
                input_size
            )
        )

        self.bias = np.random.randn()

    def activation_function(
        self,
        x
    ):
        return (
            1 if x >= 0 else 0
        )

    def predict(
        self,
        x
    ):

        linear_output = (
            np.dot(
                x,
                self.weights
            )
            + self.bias
        )

        return self.activation_function(
            linear_output
        )

    def train(
        self,
        X,
        y
    ):

        for epoch in range(
            self.epochs
        ):

            total_error = 0

            for i in range(
                len(X)
            ):

                prediction = (
                    self.predict(
                        X[i]
                    )
                )

                error = (
                    y[i]
                    - prediction
                )

                total_error += (
                    abs(error)
                )

                self.weights += (
                    self.learning_rate
                    * error
                    * X[i]
                )

                self.bias += (
                    self.learning_rate
                    * error
                )

            print(
                f"Epoch "
                f"{epoch + 1}"
                f"/{self.epochs}"
                f" | Error: "
                f"{total_error}"
            )
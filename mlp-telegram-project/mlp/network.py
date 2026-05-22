import numpy as np

from mlp.activations import (
    relu,
    softmax
)


class NeuralNetwork:

    def __init__(
        self,
        input_size,
        hidden_size,
        output_size,
        learning_rate=0.01
    ):

        self.learning_rate = (
            learning_rate
        )

        self.weights_input_hidden = (
            np.random.randn(
                input_size,
                hidden_size
            ) * 0.01
        )

        self.bias_hidden = (
            np.zeros(
                hidden_size
            )
        )

        self.weights_hidden_output = (
            np.random.randn(
                hidden_size,
                output_size
            ) * 0.01
        )

        self.bias_output = (
            np.zeros(
                output_size
            )
        )

    def forward(
        self,
        X
    ):

        self.hidden_input = (
            np.dot(
                X,
                self.weights_input_hidden
            )
            + self.bias_hidden
        )

        self.hidden_output = (
            relu(
                self.hidden_input
            )
        )

        self.final_input = (
            np.dot(
                self.hidden_output,
                self.weights_hidden_output
            )
            + self.bias_output
        )

        self.final_output = (
            softmax(
                self.final_input
            )
        )

        return (
            self.final_output
        )

    def train(
        self,
        X,
        y,
        epochs=100
    ):

        for epoch in range(
            epochs
        ):

            correct = 0

            for i in range(
                len(X)
            ):

                x_sample = X[i]

                y_sample = y[i]

                output = (
                    self.forward(
                        x_sample
                    )
                )

                prediction = (
                    np.argmax(
                        output
                    )
                )

                real_class = (
                    np.argmax(
                        y_sample
                    )
                )

                if (
                    prediction
                    == real_class
                ):
                    correct += 1

                output_error = (
                    output
                    - y_sample
                )

                hidden_error = (
                    np.dot(
                        output_error,
                        self.weights_hidden_output.T
                    )
                )

                hidden_gradient = (
                    hidden_error
                    * (
                        self.hidden_input
                        > 0
                    )
                )

                self.weights_hidden_output -= (
                    self.learning_rate
                    * np.outer(
                        self.hidden_output,
                        output_error
                    )
                )

                self.bias_output -= (
                    self.learning_rate
                    * output_error
                )

                self.weights_input_hidden -= (
                    self.learning_rate
                    * np.outer(
                        x_sample,
                        hidden_gradient
                    )
                )

                self.bias_hidden -= (
                    self.learning_rate
                    * hidden_gradient
                )

            accuracy = (
                correct
                / len(X)
            ) * 100

            print(
                f"Epoch "
                f"{epoch + 1}"
                f"/{epochs}"
                f" | Accuracy: "
                f"{accuracy:.2f}%"
            )

    def predict(
        self,
        X
    ):

        probabilities = (
            self.forward(X)
        )

        return np.argmax(
            probabilities
        )
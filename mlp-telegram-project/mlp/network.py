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
        output_size
    ):

        self.weights_input_hidden = (
            np.random.randn(
                input_size,
                hidden_size
            )
        )

        self.bias_hidden = (
            np.random.randn(
                hidden_size
            )
        )

        self.weights_hidden_output = (
            np.random.randn(
                hidden_size,
                output_size
            )
        )

        self.bias_output = (
            np.random.randn(
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

        return self.final_output
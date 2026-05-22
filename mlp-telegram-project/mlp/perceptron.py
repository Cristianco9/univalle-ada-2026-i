import numpy as np


class Perceptron:

    def __init__(
        self,
        input_size
    ):

        self.weights = (
            np.random.randn(
                input_size
            )
        )

        self.bias = np.random.randn()

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

        return (
            1
            if linear_output > 0
            else 0
        )
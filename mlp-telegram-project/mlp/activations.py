import numpy as np


def relu(x):
    return np.maximum(0, x)


def softmax(x):

    exp_values = np.exp(
        x - np.max(x)
    )

    return (
        exp_values
        / np.sum(exp_values)
    )
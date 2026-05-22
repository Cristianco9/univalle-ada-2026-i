import numpy as np


def get_simple_dataset():

    X = np.array([
        [0, 0],
        [0, 1],
        [1, 0],
        [1, 1]
    ])

    y = np.array([
        0,
        0,
        0,
        1
    ])

    return X, y


if __name__ == "__main__":

    X, y = get_simple_dataset()

    print(X)
    print(y)
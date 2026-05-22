from sklearn.datasets import load_iris
from sklearn.model_selection import (
    train_test_split
)

import numpy as np


def get_iris_dataset():

    iris = load_iris()

    X = iris.data
    y = iris.target

    X_train, X_test, y_train, y_test = (
        train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )
    )

    return (
        X_train,
        X_test,
        y_train,
        y_test
    )


if __name__ == "__main__":

    (
        X_train,
        X_test,
        y_train,
        y_test
    ) = get_iris_dataset()

    print(
        f"Train shape: {X_train.shape}"
    )

    print(
        f"Test shape: {X_test.shape}"
    )
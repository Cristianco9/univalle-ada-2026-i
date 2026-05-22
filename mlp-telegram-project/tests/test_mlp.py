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

model = NeuralNetwork(
    input_size=4,
    hidden_size=8,
    output_size=3,
    learning_rate=0.001
)

model.train(
    X_train,
    y_train_encoded,
    epochs=100
)

correct = 0

for i in range(
    len(X_test)
):

    prediction = (
        model.predict(
            X_test[i]
        )
    )

    if (
        prediction
        == y_test[i]
    ):
        correct += 1


accuracy = (
    correct
    / len(X_test)
) * 100

print(
    f"\nTest Accuracy: "
    f"{accuracy:.2f}%"
)
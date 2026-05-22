from mlp.network import (
    NeuralNetwork
)

from data.load_dataset import (
    get_iris_dataset
)

import numpy as np


(
    X_train,
    X_test,
    y_train,
    y_test
) = get_iris_dataset()


model = NeuralNetwork(
    input_size=4,
    hidden_size=8,
    output_size=3
)


sample = X_train[0]

prediction = (
    model.forward(
        sample
    )
)

print("\nPrediction probabilities:")
print(prediction)

print(
    "\nPredicted class:"
)

print(
    np.argmax(
        prediction
    )
)
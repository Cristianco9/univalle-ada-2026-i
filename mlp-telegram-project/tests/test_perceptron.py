from mlp.perceptron import (
    Perceptron
)

import numpy as np


model = Perceptron(
    input_size=4
)

sample = np.array(
    [5.1, 3.5, 1.4, 0.2]
)

prediction = (
    model.predict(
        sample
    )
)

print(
    f"Prediction: {prediction}"
)
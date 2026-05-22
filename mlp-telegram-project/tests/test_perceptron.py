from mlp.perceptron import (
    Perceptron
)

from data.simple_dataset import (
    get_simple_dataset
)


X, y = get_simple_dataset()

model = Perceptron(
    input_size=2,
    learning_rate=0.1,
    epochs=20
)

model.train(
    X,
    y
)

print("\nPredictions:")

for sample in X:

    prediction = (
        model.predict(
            sample
        )
    )

    print(
        f"{sample} -> "
        f"{prediction}"
    )
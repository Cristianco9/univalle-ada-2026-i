import numpy as np


def one_hot_encode(
    y,
    num_classes
):

    encoded = np.zeros(
        (
            len(y),
            num_classes
        )
    )

    encoded[
        np.arange(len(y)),
        y
    ] = 1

    return encoded
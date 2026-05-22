from data_structures.queue import (
    Queue
)


def create_batches(
    X,
    y,
    batch_size=16
):

    queue = Queue()

    for i in range(
        0,
        len(X),
        batch_size
    ):

        X_batch = X[
            i:i + batch_size
        ]

        y_batch = y[
            i:i + batch_size
        ]

        queue.enqueue(
            (
                X_batch,
                y_batch
            )
        )

    return queue
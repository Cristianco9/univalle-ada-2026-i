from data_structures.hash_table import (
    HashTable
)


metrics = (
    HashTable()
)

metrics.set(
    "epoch_1_loss",
    0.81
)

metrics.set(
    "epoch_2_loss",
    0.54
)

print(
    metrics.get(
        "epoch_1_loss"
    )
)

print(
    metrics.get(
        "epoch_2_loss"
    )
)
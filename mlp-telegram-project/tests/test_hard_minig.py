from algorithms.hard_mining import (
    get_hard_examples
)

losses = [
    0.2,
    0.9,
    0.1,
    0.7,
    0.95,
    0.5
]

hard_examples = (
    get_hard_examples(
        losses,
        k=3
    )
)

print(
    hard_examples
)
from algorithms.quickselect import (
    find_median
)


numbers = [
    9,
    1,
    7,
    2,
    10,
    4,
    5
]

median = (
    find_median(
        numbers
    )
)

print(
    f"Median: "
    f"{median}"
)
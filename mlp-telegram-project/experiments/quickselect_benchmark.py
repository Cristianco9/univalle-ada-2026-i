import random
import time

from algorithms.quickselect import (
    find_median
)


def benchmark():

    sizes = [
        1000,
        5000,
        10000,
        50000,
        100000
    ]

    for n in sizes:

        data = [
            random.randint(
                1,
                100000
            )
            for _ in range(n)
        ]

        start = (
            time.perf_counter()
        )

        median_qs = (
            find_median(
                data
            )
        )

        quick_time = (
            time.perf_counter()
            - start
        )

        start = (
            time.perf_counter()
        )

        sorted_data = (
            sorted(data)
        )

        median_sort = (
            sorted_data[
                len(data)//2
            ]
        )

        sort_time = (
            time.perf_counter()
            - start
        )

        print(
            f"N={n} | "
            f"Quickselect="
            f"{quick_time:.6f}s | "
            f"Sort="
            f"{sort_time:.6f}s"
        )


if __name__ == "__main__":
    benchmark()
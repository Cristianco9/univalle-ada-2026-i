import random
import time

from algorithms.top_k import (
    top_k_heap,
    top_k_sort
)


def benchmark_top_k():

    sizes = [
        1000,
        5000,
        10000,
        50000,
        100000
    ]

    k = 10

    results = []

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

        top_k_heap(
            data,
            k
        )

        heap_time = (
            time.perf_counter()
            - start
        )

        start = (
            time.perf_counter()
        )

        top_k_sort(
            data,
            k
        )

        sort_time = (
            time.perf_counter()
            - start
        )

        results.append({
            "n": n,
            "heap_time":
            heap_time,

            "sort_time":
            sort_time
        })

    return results


if __name__ == "__main__":

    results = (
        benchmark_top_k()
    )

    for r in results:

        print(
            f"N={r['n']} | "
            f"Heap="
            f"{r['heap_time']:.6f}s | "
            f"Sort="
            f"{r['sort_time']:.6f}s"
        )
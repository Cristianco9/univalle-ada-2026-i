import matplotlib.pyplot as plt

from experiments.benchmark import (
    benchmark_top_k
)


results = benchmark_top_k()

sizes = [
    r["n"]
    for r in results
]

heap_times = [
    r["heap_time"]
    for r in results
]

sort_times = [
    r["sort_time"]
    for r in results
]

plt.figure(
    figsize=(10, 5)
)

plt.plot(
    sizes,
    heap_times,
    label="Heap Top-K"
)

plt.plot(
    sizes,
    sort_times,
    label="Sort Top-K"
)

plt.xlabel(
    "Input Size (n)"
)

plt.ylabel(
    "Execution Time"
)

plt.title(
    "Heap vs Sort Top-K"
)

plt.legend()

plt.grid(True)

plt.show()
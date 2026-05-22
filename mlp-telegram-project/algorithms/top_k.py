import heapq


def top_k_heap(
    values,
    k
):

    return heapq.nlargest(
        k,
        values
    )


def top_k_sort(
    values,
    k
):

    sorted_values = sorted(
        values,
        reverse=True
    )

    return sorted_values[:k]
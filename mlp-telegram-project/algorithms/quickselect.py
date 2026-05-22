def partition(
    arr,
    low,
    high
):

    pivot = arr[high]

    i = low

    for j in range(
        low,
        high
    ):

        if arr[j] <= pivot:

            arr[i], arr[j] = (
                arr[j],
                arr[i]
            )

            i += 1

    arr[i], arr[high] = (
        arr[high],
        arr[i]
    )

    return i


def quickselect(
    arr,
    low,
    high,
    k
):

    if low == high:
        return arr[low]

    pivot_index = (
        partition(
            arr,
            low,
            high
        )
    )

    if pivot_index == k:
        return arr[k]

    elif pivot_index > k:

        return quickselect(
            arr,
            low,
            pivot_index - 1,
            k
        )

    else:

        return quickselect(
            arr,
            pivot_index + 1,
            high,
            k
        )


def find_median(
    arr
):

    copied = arr.copy()

    n = len(copied)

    median_index = n // 2

    return quickselect(
        copied,
        0,
        n - 1,
        median_index
    )
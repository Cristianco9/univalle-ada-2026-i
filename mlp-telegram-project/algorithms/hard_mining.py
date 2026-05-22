import heapq


def get_hard_examples(
    losses,
    k=5
):

    indexed_losses = [
        (
            loss,
            index
        )
        for index,
        loss
        in enumerate(losses)
    ]

    hardest = (
        heapq.nlargest(
            k,
            indexed_losses
        )
    )

    return hardest
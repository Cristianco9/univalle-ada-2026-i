from data_structures.queue import (
    Queue
)


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(
    queue.dequeue()
)

print(
    queue.dequeue()
)

print(
    queue.size()
)
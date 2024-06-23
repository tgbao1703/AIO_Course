from typing import List


class Queue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: List[float] = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def enqueue(self, value: float):
        if self.is_full():
            print("Queue is full. Cannot enqueue more items.")
            return

        self.items.append(value)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return

        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty.")
            return

        return self.items[0]

queue = Queue(capacity=5)

queue.enqueue(1)
queue.enqueue(2)

print(queue.is_full())

print(queue.front())

print(queue.dequeue())

print(queue.front())

print(queue.dequeue())

print(queue.is_empty())
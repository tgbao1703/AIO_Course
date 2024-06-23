class Stack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items: list[float] = []

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def push(self, value: float):
        if self.is_full():
            print("Stack is full. Cannot push more items.")
            return

        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop item.")
            return

        return self.items.pop()


    def top(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        return self.items[-1]

stack = Stack(capacity=5)

stack.push(1)
stack.push(2)

print(stack.is_full())

print(stack.top())

print(stack.pop())

print(stack.top())

print(stack.pop())

print(stack.is_empty())
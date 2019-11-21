class Stack:
    """LIFO stack implementation using python"""

    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def stack_length(self):
        return len(self.data)

    def pop(self):
        if self.is_empty():

            raise Empty("Stack is empty")
        else:
            return self.data.pop()

    def push(self, n):
        self.data.append(n)

    def peek(self):
        return self.data[-1]

test = Stack()

test.push(5)
test.push(8)
test.push(3)
test.push(1)
a = test.stack_length()

print(a)

print(test.pop())

print(test.stack_length())

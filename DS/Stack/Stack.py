

class Stack:
    """
    Create a stack Using an array
    Methods of a stack:
        peek(): returns top of the stack
        push(data): push the `data` into the stack
        pop(): pop the last element from the stack
        is_empty(): returns True if stack is empty else False
        capacity(): returns the current capacity of the stack
    """
    def __init__(self):
        self.stack = []
        self.top = -1
        self.capacity = 0

    def push(self, data):
        """Push an element into the stack"""
        self.stack.append(data)
        self.top += 1

    def pop(self):
        """Pop last element from stack"""
        if not self.is_empty():
            self.top -= 1
            return self.stack.pop()

    def is_empty(self):
        return self.top == 0

    def capacity(self):
        return self.top

    def peek(self):
        return self.stack[self.top]

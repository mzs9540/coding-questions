class TwoStackUsingAnArray:
    """
    Code for implementing two stacks using single array
    Methods:
        push1(data): pushes the `data` into the stack 1
        push2(data): pushes the `data` into the stack 2
        pop1(): pop from the first stack
        pop2(): pop from the second stack
        print1(): print the elements of first stack
        print2(): print the elements of second stack
        is_empty(): return True if space is available for push
        peek1(): return top element of first stack
        peek2(): return top element of second stack
    """

    def __init__(self, n):
        self.arr = [None]*n
        self.top1 = -1
        self.top2 = n

    def is_empty(self):
        return self.top2 - self.top1 > 1

    def push1(self, data):
        if self.is_empty():
            self.top1 += 1
            self.arr[self.top1] = data
        else:
            return "Array is Full"

    def push2(self, data):
        if self.is_empty():
            self.top2 -= 1
            self.arr[self.top2] = data
        else:
            return "Array is full"

    def pop1(self):
        temp = self.arr[self.top1]
        self.top1 -= 1
        return temp

    def pop2(self):
        temp = self.arr[self.top2]
        self.top2 -= 1
        return temp

    def peek1(self):
        return self.arr[self.top1]

    def peek2(self):
        return self.arr[self.top2]


if __name__ == '__main__':
    ts = TwoStackUsingAnArray(5)
    ts.push1(5)
    ts.push2(10)
    ts.push2(15)
    ts.push1(11)
    ts.push2(7)

    print("Popped element from stack1 is " + str(ts.pop1()))
    ts.push2(40)
    print("Popped element from stack2 is " + str(ts.pop2()))

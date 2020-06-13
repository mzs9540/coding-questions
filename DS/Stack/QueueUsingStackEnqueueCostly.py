from DS.Stack.Stack import Stack


class QueueUsingStack:
    """
    Class for implementing a Queue using two Stack
    By making enqueue method Costly
    Methods:
        enqueue(data): Push data into the queue at last
        dequeue(): Pop element from front of the queue
    """

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, data):
        while not self.s1.is_empty():
            temp = self.s1.pop()
            self.s2.push(temp)
        self.s1.push(data)

        while not self.s2.is_empty():
            temp = self.s2.pop()
            self.s1.push(temp)

    def dequeue(self):
        return self.s1.pop()


if __name__ == '__main__':
    q = QueueUsingStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

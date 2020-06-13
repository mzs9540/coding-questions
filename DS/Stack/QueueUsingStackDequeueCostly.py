from DS.Stack import Stack


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

    def dequeue(self):
        while not self.s1.is_empty():
            temp = self.s1.pop()
            self.s2.push(temp)
        temp1 = self.s2.pop()

        while not self.s2.is_empty():
            temp = self.s2.pop()
            self.s1.push(temp)
        return temp1

    def enqueue(self, data):
        return self.s1.push(data)

if __name__ == '__main__':
    q = QueueUsingStack()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())

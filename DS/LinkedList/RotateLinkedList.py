from LinkedList import LinkedList


class RotateLinkedList(LinkedList):
    """
    Program to rotate a linked list in clock wise or in anticlockwise
    direction(0 for clockwise and 1 for anticlockwise)
    if contains a function rotate(head, k, direction)
    """
    def __init__(self):
        LinkedList.__init__(self)

    def get_size(self, head):
        if head.next is None:
            return 1
        return 1 + self.get_size(head.next)
    
    def last_node(self, head):
        if head.next.next is None:
            prev = head
            last = head.next
            return prev, last
        return self.last_node(head.next)
    
    def rotate(self, k, direction):
        """
        Function to rotate a linked list by k nodes in clockwise or anticlockwise direction
        params:
            direction: 0 for clockwise and 1 for anticlockwise
            k: int for setting times of rotation
        """

        if self.head is None or self.head.next is None:
            return
        size = self.get_size(self.head)

        # line below will check if k is greater than size than reduce it
        # because after no. of rotation equals to size the linked list will
        # comes in it's initial condition
        k = k % size
        if not direction:
            while k > 0:
                prev, last = self.last_node(self.head)
                last.next = self.head
                self.head = last
                prev.next = None
                k -= 1
        else:
            while k > 0:
                prev, last = self.last_node(self.head)
                last.next = self.head
                self.head = self.head.next
                last.next.next = None
                k -= 1

        return self.head


if __name__ == '__main__':
    llist = RotateLinkedList()
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    llist.print_list()
    llist.rotate(6, 0)
    llist.print_list()

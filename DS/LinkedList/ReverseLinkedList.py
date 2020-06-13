from DS.LinkedList import LinkedList


class ReverseLinkedList(LinkedList):

    # Function to initialize head
    def __init__(self):
        super().__init__()
        self.temp_head = None

    def reverse_util(self, curr, prev):
        if curr.next is not None:
            self.reverse_util(curr.next, curr)

        # If last node mark it head
        if curr.next is None:
            self.temp_head = curr

        if curr.data == self.head.data:
            self.head = self.temp_head
            curr.next = None
            return

        curr.next = prev

    def reverse(self):
        if self.head is None:
            return
        self.reverse_util(self.head, None)


if __name__ == '__main__':
    llist = ReverseLinkedList()
    llist.push(8)
    llist.push(7)
    llist.push(6)
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print(llist.head.data)
    llist.print_list()
    llist.reverse()
    print(llist.head.data)
    llist.print_list()

from DS.LinkedList import LinkedList


class ReverseNodesBunch(LinkedList):
    """
    Reverse every n nodes in the linked list
    """

    def __init__(self):
        self.temp_head = None
        super().__init__()

    def reverse_n_bunch(self, head, n):
        """Method for reversing n bunch of a linked list"""

        curr = head
        prev = None
        k = 0
        while curr is not None and k < n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            k += 1

        if curr:
            head.next = self.reverse_n_bunch(curr, n)

        return prev


if __name__ == '__main__':
    llist = ReverseNodesBunch()
    llist.create_from_list([9, 8, 7, 6, 5, 4, 3, 2, 1])
    llist.print_list()
    llist.head = llist.reverse_n_bunch(llist.head, 3)
    llist.print_list()

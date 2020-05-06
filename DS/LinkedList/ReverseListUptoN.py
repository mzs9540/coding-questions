from datetime import datetime

from LinkedList import LinkedList


class ReverseListUptoN(LinkedList):

    def __init__(self):
        self.temp = None
        self.temp_h = None
        super().__init__()

    def reverse_upto_n(self, curr, prev, n):
        if not curr:
            self.temp = curr
            return

        if n > 0:
            print(curr.data)
            self.reverse_upto_n(curr.next, curr, n-1)

        if n == 0:
            print('n=0', curr.data)
            self.temp = curr
            self.get_head().next = curr
            self.update_head(prev)
            return

        if self.temp == curr:
            return

        curr.next = prev

    def reverse_n(self, curr, n):
        if curr is None or curr.next is None:
            return
        self.temp = curr
        prev = None
        self.reverse_upto_n(curr, prev, n)


if __name__ == '__main__':
    llist = ReverseListUptoN()
    llist.create_from_list([9, 8, 7, 6, 5, 4, 3, 2, 1])
    llist.print_list()
    llist.reverse_n(llist.head, 3)
    llist.print_list()

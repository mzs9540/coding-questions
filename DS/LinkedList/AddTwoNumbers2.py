from LinkedList import LinkedList
from LinkedList import Node


def prepend_zeros(head, extra):
    """Add extra zeros in the beginning"""
    while extra > 0:
        node = Node(0)
        temp = head
        head = node
        head.next = temp
        extra -= 1
    return head


def get_size(head):
    """Calculate The size of the Linked List"""
    if head is None:
        return 0
    return get_size(head.next) + 1


class AddTwoNumbers2(LinkedList):
    """
    Add two number represented by a Linked List
    num1 = 5->3->2 represent 532
    """

    def __init__(self):
        LinkedList.__init__(self)
        self.car = 0
        self.temp_head = None

    def add_helper(self, head1, head2):
        if head1 is None and head2 is None:
            print('hoooollaaa')
            return None
        temp = self.add_helper(head1.next, head2.next)
        res = head1.data + head2.data + self.car
        self.car = int(res/10)
        res = int(res % 10)
        self.temp_head = Node(res)
        self.temp_head.next = temp
        print(self.temp_head.data, 'temp_head')
        return self.temp_head

    def add(self, head1, head2):
        len1 = get_size(head1)
        len2 = get_size(head2)
        if len1 > len2:
            head2 = prepend_zeros(head2, len1 - len2)
        else:
            head1 = prepend_zeros(head1, len2 - len1)
        self.add_helper(head1, head2)
        if self.car:
            temp = self.temp_head
            self.temp_head = Node(self.car)
            self.temp_head.next = temp
        self.head = self.temp_head
        return self.temp_head


if __name__ == '__main__':
    first = AddTwoNumbers2()
    second = AddTwoNumbers2()
    # Create first list

    first.push(4)
    first.push(3)
    first.push(9)
    first.print_list()

    # Create second list
    second.push(4)
    second.push(8)
    second.print_list()

    result = AddTwoNumbers2()
    result.add(first.head, second.head)
    result.print_list()


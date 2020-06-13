from DS.LinkedList import Node
from DS.LinkedList import LinkedList


class AddTwoNumber(LinkedList, Node):
    """
    Class for adding Two numbers represented by Linked List
    This Class Contains Method add_numbers which takes two arguments
    both are heads of linked list which represent the numbers
    """

    def __init__(self):
        LinkedList.__init__(self)
        self.t_head = None

    def add_two_numbers(self, head1, head2, carry):

        if head1 and head2:
            result = head1.data + head2.data + carry
            carry = int(result / 10)
            result = int(result % 10)
            temp = Node(result)
            temp.next = self.add_two_numbers(head1.next, head2.next, carry)
            return temp

        if head1 and not head2:
            result = head1.data + carry
            carry = int(result/10)
            result = int(result % 10)
            temp = Node(result)
            temp.next = self.add_two_numbers(head1.next, None, carry)
            return temp

        if head2 and not head1:
            result = head2.data + carry
            carry = int(result/10)
            result = int(result % 10)
            temp = Node(result)
            temp.next = self.add_two_numbers(None, head2.next, carry)
            return temp

        if carry:
            print('in carry', carry)
            temp = Node(int(carry))
            return temp

        if not head1 and not head2 and not carry:
            return None

    def add_numbers(self, head1, head2):
        result = self.add_two_numbers(head1, head2, 0)
        return result


if __name__ == '__main__':
    first = AddTwoNumber()
    second = AddTwoNumber()

    # Create first list
    first.push(6)
    first.push(4)
    first.push(9)
    first.push(5)
    first.push(7)
    first.print_list()

    # Create second list
    second.push(4)
    second.push(8)
    second.print_list()

    # Add the two lists and see result
    res = AddTwoNumber()
    res.head = res.add_numbers(first.head, second.head)
    res.print_list()

    # Lesson Learnt if we use self.t_head in return in place of
    # temp then it causes error because it has global scope it will available to every
    # recursion stack

class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to print the linked LinkedList
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next


if __name__ == '__main__':
    llist = LinkedList()
    llist.push(15)
    llist.push(13)
    llist.push(11)
    llist.push(9)
    llist.push(7)
    llist.push(5)
    llist.push(3)
    llist.push(1)

    llist1 = LinkedList()
    llist1.push(14)
    llist1.push(12)
    llist1.push(10)
    llist1.push(8)
    llist1.push(6)
    llist1.push(4)
    llist1.push(2)

    def merge_two_list(head1, head2):
        """Merge two sorted Linked List"""
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.data <= head2.data:
            temp = head1
            temp.next = merge_two_list(head1.next, head2)

        else:
            temp = head2
            temp.next = merge_two_list(head1, head2.next)

        return temp

    llist2 = LinkedList()
    llist2.head = merge_two_list(llist.head, llist1.head)
    llist2.print_list()

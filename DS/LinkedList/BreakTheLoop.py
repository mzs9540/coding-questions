from LinkedList import LinkedList


class BreakTheLoop(LinkedList):
    """Class for detecting the Loop in the Linked list and removing it"""

    def __init__(self):
        super().__init__()

    def loop_detect_and_return_node(self, head):
        """Detect Loop and return the intersection Node"""

        slow = head
        fast = head
        flag = True
        while flag:
            slow = slow.next
            fast = fast.next.next

            if slow.data == fast.data:
                print(fast.data, slow.data)
                flag = False

            if fast.next is None or fast.next.next is None:
                print("No loop")

        else:
            ptr = head
            prev = None
            while ptr != slow:
                print(ptr.data, slow.data)
                ptr = ptr.next
                prev = slow
                slow = slow.next
            prev.next = None


if __name__ == '__main__':
    llist = BreakTheLoop()
    llist.push(10)
    llist.push(4)
    llist.push(15)
    llist.push(20)
    llist.push(50)

    # Create a loop for testing
    llist.loop_detect_and_return_node(llist.head)
    llist.print_list()

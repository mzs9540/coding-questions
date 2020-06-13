from DS.LinkedList import LinkedList


def find_middle(h):
    slow = fast = h
    while not fast.next and not fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow


class MergeSort(LinkedList):

    def merge(self, left, right):

        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)

        return result

    def merge_sort(self, t_head):
        if not t_head or not t_head.next:
            return t_head
        m = find_middle(t_head)
        m_next = m.next
        m.next = None
        left = self.merge_sort(t_head)
        right = self.merge_sort(m_next)
        return self.merge(left, right)


if __name__ == '__main__':

    llist = MergeSort()
    llist.push(2)
    llist.push(13)
    llist.push(1)
    llist.push(5)
    llist.push(9)
    llist.push(3)
    llist.push(0)
    llist.push(1)
    llist.print_list()
    llist.head = llist.merge_sort(llist.head)
    llist.print_list()

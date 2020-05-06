class Node:

    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def update_head(self, head):
        self.head = head

    def get_head(self):
        return self.head

    def create_from_list(self, ar):
        """Create a Linked List by passing an array"""
        for data in ar:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

        return self.head

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
        print()

from Stack import Stack


class NextGreater(Stack):
    """
    Program to print next greater element in the array
    Methods:
        print_greater(arr) -> return next greater of every element in the array
    """
    def __init__(self):
        self.next = -1
        Stack.__init__(self)

    def print_greater(self, arr):
        self.push(arr[0])
        self.next = arr[1]
        for i in arr[1:]:
            self.next = i
            if i <= self.peek():
                self.push(i)
            else:
                while not self.is_empty() and self.next > self.peek():
                    temp = self.pop()
                    print(f'Next Greater of {temp} is {self.next}')
                self.push(i)
        while not self.is_empty():
            temp = self.pop()
            print(f'Next Greater of {temp} is -1')


if __name__ == '__main__':
    array = [60, 2, 6, 4, 7, 13, 11, 10, 9, 23, 56]
    next_greater = NextGreater()
    next_greater.print_greater(array)


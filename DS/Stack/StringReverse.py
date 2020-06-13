from DS.Stack import Stack


class StringReverse(Stack):
    """
    Reverse String using Stack
    methods:
        reverse(string): reverse the passed string using stack
        print(): print the reversed string
    """

    def __init__(self):
        Stack.__init__(self)
        self.string = ''

    def reverse(self, s):
        for i in s:
            self.push(i)

        while not self.is_empty():
            self.string += str(self.pop())

    def print(self):
        print(self.string)


if __name__ == '__main__':
    string = StringReverse()
    string.reverse('String')
    string.print()

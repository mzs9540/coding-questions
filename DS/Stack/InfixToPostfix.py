from Stack import Stack

preferences = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


def is_operator(op):
    """Return True if operator"""
    return op in preferences


class InfixToPostfix(Stack):
    """Program to convert infix expression to postfix"""

    def __init__(self):
        Stack.__init__(self)
        self.postfix = ''

    def infix_to_postfix(self, e):
        """Convert Infix expression to postfix"""
        self.push('(')
        exp = e + ')'
        for i in exp:
            print(i, self.peek(), self.postfix)
            if is_operator(i):
                while is_operator(i) and is_operator(self.peek()) and (preferences[self.peek()] >= preferences[i]):
                    self.postfix += str(self.pop())
                self.push(i)

            elif i == '(':
                self.push(i)

            elif i == ')':
                while self.peek() != '(':
                    pop = self.pop()
                    self.postfix += str(pop)
                self.pop()
            elif i.isalnum():
                self.postfix += str(i)

            else:
                print('Invalid Expression')

    def print_postfix(self):
        print(self.postfix)


if __name__ == '__main__':
    stack = InfixToPostfix()
    ex = "a+b*(c^d-e)^(f+g*h)-i"
    stack.infix_to_postfix(ex)
    stack.print_postfix()

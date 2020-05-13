from Stack import Stack


def is_operator(op):
    """Return True if operator"""
    return op in ['^', '/', '*', '+', '-']


class PostfixToInfix(Stack):
    """Program to convert infix expression to postfix"""

    def __init__(self):
        Stack.__init__(self)
        self.infix = ''

    def postfix_to_infix(self, e):
        """Convert Infix expression to postfix"""
        for i in e:
            if is_operator(i):
                operand2 = self.pop()
                operand1 = self.pop()
                res = operand1 + i + operand2
                self.push(str(eval(res)))
            else:
                self.push(i)

    def print_infix(self):
        print(self.stack[0])


if __name__ == '__main__':
    stack = PostfixToInfix()
    ex = "231*+9-"
    stack.postfix_to_infix(ex)
    stack.print_infix()

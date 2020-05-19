from Stack import Stack


class BalancedParenthesis(Stack):
    """
    Code to check the order and balancing of parenthesis
    Methods:
        check(): check the order and balancing of the parenthesis and return True if Balanced
    """
    def __init__(self, st):
        self.st = st
        self.order = {
            '(': 1, ')': 4, '{': 3, '}': 6, '[': 2, ']': 5
        }
        Stack.__init__(self)

    def check(self):
        for s in self.st:
            if self.order[s] <= 3:
                if self.top == -1 or self.order[s] <= self.order[self.peek()]:
                    self.push(s)
                else:
                    return False
            else:
                if self.order[self.peek()] == self.order[s] - 3:
                    self.pop()
                    return False
        return True


if __name__ == '__main__':
    expr = "{()}[]"
    check = BalancedParenthesis(expr)
    if check.check():
        print("Balanced")
    else:
        print("Not Balanced")

from DS.Stack.Stack import Stack


class BalancedParenthesis(Stack):
    def __init__(self):
        self.order = {
            '(': 1, ')': 4, '{': 3, '}': 6, '[': 2, ']': 5
        }
        Stack.__init__(self)

    def check(self, st):
        for s in st:
            if self.order[s] <= 3:
                self.push(s)
            else:
                if not self.is_empty() and self.order[self.peek()] == self.order[s] - 3:
                    self.pop()
                else:
                    return False
        if self.is_empty():
            return True
        else:
            return False


if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        expr = input()
        arr.append(expr)

    for ex in arr:
        check = BalancedParenthesis()
        if check.check(ex):
            print("YES")
        else:
            print("NO")

def enqueue(s1, data):
    s1.append(data)


def dequeue(s1):
    temp = s1.pop(0)
    return temp


def head(s1):
    return s1[0]


def tail(s1):
       return s1[-1]


if __name__ == '__main__':
    s1 = []
    q = int(input())
    for _ in range(q):
        op = input()
        if len(op) > 1:
            enqueue(s1, op.split()[1])
        elif op == '2':
            dequeue(s1)
        else:
            print(head(s1))

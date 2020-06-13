def piling_up(n, array):
    pushed_index = 0 if array[0] >= array[-1] else n-1
    front = 0
    back = n-1
    if pushed_index == 0:
        front = 1
    else:
        back = n-2
    while front <= back:
        if array[pushed_index] < array[front] or array[pushed_index] < array[back]:
            print(array[pushed_index], array[front], array[back])
            return 'No'
        pushed_index = front if array[front] >= array[back] else back
        if pushed_index == front:
            front += 1
        else:
            back -= 1
    return 'Yes'


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(piling_up(n, arr))

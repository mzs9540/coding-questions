def re_arrange(array):
    arr_len = len(array)
    k = 0
    for i in range(arr_len):
        if array[i]:
            array[k] = array[i]
            k = k + 1


def merge(array_big, array_small):
    len_big = len(array_big)
    len_small = len(array_small)

    i = len_big - len_small - 1
    j = len_small - 1
    k = len_big - 1

    while i >= 0 and j >= 0:
        if array_big[i] >= array_small[j]:
            array_big[k] = array_big[i]
            i -= 1
        if array_big[i] < array_small[j]:
            array_big[k] = array_small[j]
            j -= 1
        k -= 1

    while j >= 0:
        array_big[j] = array_small[j]
        j -= 1


if __name__ == '__main__':
    arr_big = [0, 2, 0, 3, 0, 5]
    arr_small = [0, 1, 9]

    re_arrange(arr_big)
    merge(arr_big, arr_small)

    print(arr_big)

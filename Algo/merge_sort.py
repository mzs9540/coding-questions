def merge_sort(arr):
    """
    Function to apply merge sort on an array of numbers
    :param arr: takes an array of numbers
    :return: sorted array of numbers
    """

    def merge(left, middle, right):
        l_half = arr[left:middle+1]
        r_half = arr[middle+1:right+1]
        l_len = len(l_half)
        r_len = len(r_half)
        i = j = 0
        k = left
        while i < l_len and j < r_len:
            if l_half[i] >= r_half[j]:
                arr[k] = r_half[j]
                j += 1
                k += 1
            else:
                arr[k] = l_half[i]
                i += 1
                k += 1
        while i < l_len:
            arr[k] = l_half[i]
            k += 1
            i += 1
        while j < r_len:
            arr[k] = r_half[j]
            k += 1
            j += 1

    def sort(left, right):
        if left < right:
            middle = (right + left) // 2
            sort(left, middle)
            sort(middle + 1, right)
            merge(left, middle, right)

    sort(0, len(arr) - 1)
    return arr


if __name__ == '__main__':
    array = [1, 3, 2, 33, 23, 45, 55]
    res = merge_sort(array)
    print(res)

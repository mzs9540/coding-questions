def get_array_sum(array, array_len):
    array_sum = 0
    for i in range(array_len):
        array_sum += array[i]
    return array_sum


def get_equilibrium_index(array):
    n = len(array)
    total = get_array_sum(array, n)
    indices = []

    current_sum = 0
    for i in range(n):
        if current_sum == total - array[i] - current_sum:
            indices.append(i)

        current_sum += array[i]
    return indices


if __name__ == '__main__':
    arr = [0, -3, 5, -4, -2, 3, 1, 0]

    indices_final = get_equilibrium_index(arr)
    print(indices_final)

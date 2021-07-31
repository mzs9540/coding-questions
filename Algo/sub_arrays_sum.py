from typing import List


def insert_dict(dictionary: dict, key: int, value: int):
    dictionary.setdefault(key, []).append(value)


def print_all_sublist(arr: List[int]):
    sum_index_dict = {}
    sum_current = 0

    insert_dict(sum_index_dict, 0, -1)

    for i in range(len(arr)):
        sum_current += arr[i]
        if sum_current in sum_index_dict:
            index_list = sum_index_dict.get(sum_current)

            for item in index_list:
                print('Sublist', item + 1, i)

        insert_dict(sum_index_dict, sum_current, i)


if __name__ == '__main__':
    array = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2, 3]
    print_all_sublist(array)

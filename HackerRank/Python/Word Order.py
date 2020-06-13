from collections import OrderedDict


def word_order():
    words = OrderedDict()

    for _ in range(int(input())):
        word = input()
        words.setdefault(word, 0)
        words[word] += 1

    print(len(words))
    print(*words.values())


if __name__ == '__main__':
    word_order()

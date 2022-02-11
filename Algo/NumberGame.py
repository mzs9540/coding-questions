import math


class NumberGame:
    def calc_score(self, numbers: [int]):
        def calc(nums, scores):
            if not nums:
                return 0
            if tuple(nums) in scores:
                return scores[tuple(nums)]
            n = len(nums) / 2
            max_score = 0
            for i in range(int(2 * n)):
                for j in range(i + 1, int(2 * n)):
                    a = nums[i]
                    b = nums[j]
                    nums_copy = nums.copy()
                    nums_copy.remove(a)
                    nums_copy.remove(b)
                    score = int(n * math.gcd(a, b)) + calc(nums_copy, scores)

                    if score > max_score:
                        max_score = score
            scores[tuple(nums)] = max_score
            return max_score
        return calc(numbers, {})


if __name__ == '__main__':
    game = NumberGame()
    res1 = game.calc_score([1, 2, 3, 4, 5, 6])
    res2 = game.calc_score([1, 2])
    res3 = game.calc_score([3, 4, 6, 8])
    print(res1)
    print(res2)
    print(res3)

class Solution(object):
    def better(self, nums):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)

    def missingNumber(self, nums):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        import operator
        from functools import reduce
        a = reduce(operator.xor, nums)
        b = reduce(operator.xor, range(len(nums) + 1))
        return a ^ b

    def other(self, nums):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = 0
        for num in nums + list(range(len(nums) + 1)):
            result ^= num
        return result


def main():
    args = [
        [0],
        [1],
        [1, 0],
        [0, 1],
        [0, 2],
        [1, 2],
        [0, 1, 3],
    ]
    solution = Solution()
    for arg in args:
        print('****************************')
        # print(solution.missingNumber(arg))
        print(solution.better(arg))
        print(solution.other(arg))


if __name__ == '__main__':
    main()

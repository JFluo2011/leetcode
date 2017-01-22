class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        tmp = 5
        while n >= tmp:
            count += n // tmp
            tmp *= 5

        return count


def main():
    solution = Solution()
    args = [
        0,
        5,
        10,
        12,
        25,
        100,
        2527,
    ]
    for arg in args:
        print(arg, solution.trailingZeroes(arg))


if __name__ == '__main__':
    main()

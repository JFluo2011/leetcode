class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        return int(x**0.5) if x >= 0 else x


def main():
    a = 0
    solution = Solution()
    print(solution.mySqrt(a))


if __name__ == '__main__':
    main()

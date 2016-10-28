class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        return x**n


def main():
    a = 8.88023
    b = 3
    solution = Solution()
    print(solution.myPow(a, b))


if __name__ == '__main__':
    main()

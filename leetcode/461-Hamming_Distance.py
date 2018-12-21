class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')


def main():
    a = 11
    b = 10
    solution = Solution()
    print(solution.hammingDistance(a, b))


if __name__ == '__main__':
    main()

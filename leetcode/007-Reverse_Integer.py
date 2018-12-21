class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)[::-1]
        result = int('-' + s[:-1]) if s[-1] == '-' else int(s)
        return result if (result < 2147483647) and (result > -2147483648) else 0


def main():
    solution = Solution()
    print(solution.reverse(-321))


if __name__ == '__main__':
    main()
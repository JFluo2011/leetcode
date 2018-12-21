class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        return str(int(num1) * int(num2))


def main():
    num1 = '2'
    num2 = '3'
    solution = Solution()
    print(solution.multiply(num1, num2))


if __name__ == '__main__':
    main()

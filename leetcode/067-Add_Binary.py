class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return bin(int(str(int(a, 2) + int(b, 2))))[2:]


def main():
    a = '11'
    b = '10'
    solution = Solution()
    print(solution.addBinary(a, b))


if __name__ == '__main__':
    main()

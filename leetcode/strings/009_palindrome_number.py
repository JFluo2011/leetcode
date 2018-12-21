class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return (x == abs(x)) and (str(abs(x)) == str(abs(x))[::-1])
        return int(str(abs(x))[::-1]) == x


def main():
    args = [
        0,
        121,
        -121,
        +121,
        10,
        1212,
        1221,
    ]
    solution = Solution()
    for arg in args:
        print(solution.isPalindrome(arg))


if __name__ == '__main__':
    main()

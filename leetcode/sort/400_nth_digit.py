class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        while True:
            first = 10**(digit-1)
            cnt = 9 * first * digit
            if cnt >= n:
                return int(str(first + (n-1)//digit)[(n-1) % digit])
            n -= cnt
            digit += 1


def main():
    args = [
        # (0, 0),
        # (3, 3),
        (9, 9),
        # (11, 0),
        # (21, 5),
        (1000, 3),
        # (100000000, 3),
    ]
    solution = Solution()
    for arg, result in args:
        try:
            assert solution.findNthDigit(arg) == result
        except AssertionError:
            print(arg)
            raise AssertionError


if __name__ == '__main__':
    main()

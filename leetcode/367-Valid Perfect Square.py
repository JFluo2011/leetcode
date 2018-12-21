class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # 39 ms #
        if num == 0:
            return False
        left, right = 0, num
        while left <= right:
            mid = (left + right) / 2
            if mid * mid > num:
                right = mid - 1
            elif mid * mid < num:
                left = mid + 1
            else:
                return True
        return False
        # 66 ms #
        # if num == 0:
        #     return False
        # i = 1
        # while num > 0:
        #     num -= i
        #     i += 2
        #
        # return num == 0
        # 75 ms #
        # return True if (num > 0) and (num**0.5 == int(num**0.5)) else False


def main():
    a = 0
    solution = Solution()
    print(solution.isPerfectSquare(a))


if __name__ == '__main__':
    main()

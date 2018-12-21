class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 56ms #
        # flag = 1
        # for i in range(len(digits)-1, -1, -1):
        #     if not flag:
        #         break
        #     if digits[i] + flag == 10:
        #         digits[i] = 0
        #     else:
        #         digits[i] += flag
        #         flag = 0
        # if flag:
        #     digits.insert(0, 1)
        # return digits
        # 72 ms #
        # length = len(digits)
        # digits[length - 1] += 1
        # while length > 0:
        #     if digits[length-1] == 10:
        #         digits[length-1] = 0
        #         if length-2 >= 0:
        #             digits[length-2] += 1
        #         else:
        #             digits.insert(0, 1)
        #     length -= 1
        # return digits
        # 58ms #
        result = 1
        for index, value in enumerate(digits[::-1]):
            result += value * 10 ** index
        return [int(i) for i in str(result)]


def main():
    l = [9]
    solution = Solution()
    print(solution.plusOne(l))


if __name__ == '__main__':
    main()

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: s
        :rtype: int
        """
        s = s.strip()
        sign = ''
        if s and ((s[0] == '+') or (s[0] == '-')):
            sign = s[0]
            s = s[1:]
        l = []
        for i in list(s):
            if i.isdigit():
                l.append(i)
            else:
                break
        if not l:
            return 0
        result = int(str('-' + ''.join(l))) if sign == '-' else int(str(''.join(l)))
        if result > 2147483647:
            result = 2147483647
        elif result < -2147483648:
            result = -2147483648
        return result


def main():
    l = ["", "+", "-", "-2", "+-", "+-2", "+++++2", "+2", '1', "    010", "  -0012a42"]
    solution = Solution()
    for i in l:
        print(solution.myAtoi(i))


if __name__ == '__main__':
    main()

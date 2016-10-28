from collections import Counter


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: s
        :rtype: int
        """
        if not ''.join([i for i in list(s) if (i != '+') and (i != '-')]).isdigit():
            return 0
        d = Counter(s)
        l = [i for i in list(s) if (i != '+') and (i != '-')]
        if d['-'] % 2 != 0:
            l.insert(0, '-')
        return int(str(''.join(l)))


def main():
    solution = Solution()
    print(solution.myAtoi("+-2"))


if __name__ == '__main__':
    main()

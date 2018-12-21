class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        tmp = ['' for i in range(numRows)]
        row = 0
        step = 1
        for i in range(len(s)):
            if row == 0:
                step = 1
            elif row == numRows-1:
                step = -1
            tmp[row] += s[i]
            row += step
        return ''.join(tmp)


def main():
    solution = Solution()
    print(solution.convert("PAYPALISHIRING", 3))


if __name__ == '__main__':
    main()

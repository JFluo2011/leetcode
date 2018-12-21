class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        return self.o_n2(s)

    def o_n2(self, s):
        start, max_len = 0, 1
        for i in range(len(s)):
            start, max_len = self.helper(s, i-1, i+1, start, max_len)
            start, max_len = self.helper(s, i, i+1, start, max_len)

        return s[start: start+max_len]

    def helper(self, s, l, r, start, max_len):
        while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
            if max_len < (r - l + 1):
                max_len = r - l + 1
                start = l
            l -= 1
            r += 1

        return start, max_len


def main():
    args = [
        '',
        'a',
        'ab',
        'aa',
        'aab',
        'abb',
        'aabb',
        'abba',
        'babad',
        'bbbbbb',
        'bbbbbbb',
    ]
    solution = Solution()
    for arg in args:
        print(solution.longestPalindrome(arg))


if __name__ == '__main__':
    main()

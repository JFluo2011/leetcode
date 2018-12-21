class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return self.my_solution(s)
        return self.greate_one(s)

    def my_solution(self, s):
        num, seen = 0, set()
        for e in s:
            if e in seen:
                num += 2
                seen.remove(e)
            else:
                seen.add(e)
        return (num + 1) if (len(seen) != 0) else num

    def greate_one(self, s):
        from collections import Counter
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)


def main():
    args = [
        '',
        'bb',
        'bbc',
        'bbbbbbbb',
        'bbbbbbbbb',
        'abcc',
        'bbcc',
        'abccb',
        'abccccdd',
    ]
    solution = Solution()
    for arg in args:
        print(solution.longestPalindrome(arg))


if __name__ == '__main__':
    main()

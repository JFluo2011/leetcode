class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        from functools import cmp_to_key
        d = sorted(d, key=cmp_to_key(lambda x, y: len(x) - len(y) if len(x) != len(y) else (x < y) - (x > y)), reverse=True)
        for t in d:
            i2 = 0
            for i1, v in enumerate(s):
                if v == t[i2]:
                    i2 += 1
                if i2 == len(t):
                    return t
        return ''


def main():
    s = Solution()
    print(s.findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))


if __name__ == '__main__':
    main()

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return Counter(s) == Counter(t)


def main():
    s = Solution()
    s.isAnagram("anagram", "nagaram")


if __name__ == '__main__':
    main()

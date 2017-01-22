from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)

    def better(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return Counter(s) == Counter(t)


def main():
    args = [
        ["", ""],
        ['go go go','gggooo'],
        ["anagram", "nagaram"],
        ["rat", "car"],
    ]
    solution = Solution()
    for arg in args:
        print(arg)
        print("solution1: {}".format(solution.isAnagram(*arg)))
        print("solution2: {}\n".format(solution.better(*arg)))


if __name__ == '__main__':
    main()

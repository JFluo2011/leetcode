class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(_ for _ in s.lower() if _.isalnum())
        return s == s[::-1]
        # s = s.lower()
        # left, right = 0, len(s)-1
        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #         continue
        #     if not s[right].isalnum():
        #         right -= 1
        #         continue
        #     if s[left] != s[right]:
        #         return False
        #     left += 1
        #     right -= 1
        # else:
        #     return True


def main():
    args = [
        '',
        '0P',
        '@$@$$@$',
        'A man, a plan, a canal: Panama',
        'race a car',
    ]
    solution = Solution()
    for arg in args:
        print(solution.isPalindrome(arg))


if __name__ == '__main__':
    main()

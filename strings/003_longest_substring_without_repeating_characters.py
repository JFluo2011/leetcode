class Solution:
    def length_of_longest_substring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # return self.o_2n(s)
        return self.o_n(s)

    def o_2n(self, s):
        # worst case: O(2n)
        i, j, length = 0, 0, 0
        seen = set()
        while j < len(s):
            if s[j] not in seen:
                seen.add(s[j])
                j += 1
            else:
                length = max((j - i),  length)
                seen.remove(s[i])
                i += 1
        else:
            length = max((j - i), length)

        return length

    def o_n(self, s):
        # O(n)
        # i: 字串起点 j:字串终点
        i, j, length = 0, 0, 0
        # 存储每个字符的value: index+1
        dct = {}
        while j < len(s):
            if s[j] in dct.keys():
                # 取出字串最大起始位置
                i = max(dct[s[j]], i)
            # 初始化/更新字符s[j]的value: index+1
            dct[s[j]] = j + 1
            j += 1
            # 计算无重复字串长度
            length = max((j - i), length)

        return length


def main():
    args = [
        '',
        'abba',
        'abcdef',
        'abcabcbb',
        'aaabb',
        'bbbbb',
        'pwwkew',
        'pwxawkew',
        'wpbwxakwjw',
    ]
    solution = Solution()
    for arg in args:
        print(solution.length_of_longest_substring(arg))


if __name__ == '__main__':
    main()

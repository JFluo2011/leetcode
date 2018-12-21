class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        max_value = 0
        for num in nums:
            if num > 0:
                if num not in d:
                    d[num] = 1
                if max_value < num:
                    max_value = num
        for num in range(1, max_value):
            if not d[num]:
                return num
        else:
            return max_value + 1


def main():
    args = [
        [],
        [1, 1],
        [1000, -1],
        [1, 1000],
        [-1, -2, -3],
        [1, 2, 0],
        [3, 4, -1, 1],
        [3, 4, 5],
    ]
    solution = Solution()
    for arg in args:
        print('****************************')
        print(solution.firstMissingPositive(arg))


if __name__ == '__main__':
    main()

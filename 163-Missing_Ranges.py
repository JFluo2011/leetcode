class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        d = defaultdict(int)
        max_value = 0
        results = []
        for num in nums:
            if num > 0:
                if num not in d:
                    d[num] = 1
                if max_value < num:
                    max_value = num
        result = []
        for num in range(100):
            if not d[num]:
                result.append(num)
            else:
                results.append(result)
                result = []
        else:
            if result:
                results.append(result)

        return [result if len(result) <= 1 else '{}->{}'.format(result[0], result[-1])
                for result in results[1:]]


def main():
    args = [
        [0, 1, 3, 50, 75],  # ['2', '4->49', '51->74', '76->99']
    ]
    solution = Solution()
    for arg in args:
        print('****************************')
        print(solution.firstMissingPositive(arg))


if __name__ == '__main__':
    main()

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        d = defaultdict(int)
        for num in candidates:
            if num not in d:
                d[num] = 1
        sub = 0
        results = []
        pass

def main():
    args = [
        [[2, 3, 6, 7], 7],
    ]
    solution = Solution()
    for arg in args:
        print('****************************')
        print(solution.combinationSum(arg))


if __name__ == '__main__':
    main()

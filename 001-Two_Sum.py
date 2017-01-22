class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        temp_nums = sorted(nums)
        index_list = self.sum(temp_nums, 0, len(temp_nums)-1, target)
        if index_list[0] == index_list[1]:
            return [i for (i,j) in enumerate(nums) if index_list[0] == j][:2]
        else:
            return [nums.index(i) for i in index_list]

    def sum(self, nums, first, end, target):
        if nums[first] + nums[end] < target:
            first += 1
        elif nums[first] + nums[end] > target:
            end -= 1
        else:
            return [nums[first], nums[end]]
        return self.sum(nums, first, end, target)

    def better(self, nums, target):
        d = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in d:
                return d[diff], index
            d[value] = index


def main():
    solution = Solution()
    print(solution.better([0, 4, 3, 0], 0))
    print(solution.better([3, 2, 4], 6))


if __name__ == '__main__':
    main()

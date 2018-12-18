class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return [nums]
        result = []
        self.helper(nums, 0, result)
        return result

    def helper(self, nums, index, result):
        if index == len(nums):
            result.append(nums[:])
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.helper(nums, index+1, result)
            nums[i], nums[index] = nums[index], nums[i]


def main():
    s = Solution()
    print(s.permute([1, 2, 3]))


if __name__ == '__main__':
    main()

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index, length = 0, len(nums)
        for num in nums:
            if num != 0:
                nums[index] = num
                index += 1

        nums[index:] = [0] * (length-index)

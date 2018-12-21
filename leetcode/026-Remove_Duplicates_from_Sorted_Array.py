class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        temp, current = nums[0], 1
        for num in nums[1:]:
            if temp ^ num != 0:
                nums[current] = num
                current += 1
            temp = num
        return current

        # if not nums:
        #     return 0
        # temp, current, length = nums[0], 1, len(nums)
        # nums.append(nums[0])
        # for i in range(1, length):
        #     if temp ^ nums[i] != 0:
        #         nums[current] = nums[i]
        #         current += 1
        #     temp = nums[i]
        # return current

class Solution:
    count = 0
    result = 0

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [str(i) for i in range(1, n+1)]
        self.helper(nums, 0, k)
        return self.result

    def helper(self, nums, index, k):
        if index == len(nums):
            self.count += 1
            if k == self.count:
                self.result = ''.join(nums)
                return
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.helper(nums, index+1, k)
            if k == self.count:
                break
            nums[i], nums[index] = nums[index], nums[i]


def main():
    s = Solution()
    print(s.getPermutation(9, 3))


if __name__ == '__main__':
    main()

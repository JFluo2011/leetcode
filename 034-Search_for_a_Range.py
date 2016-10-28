class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1
        left_found, right_found = False, False
        while (not left_found or not right_found) and (left <= right):
            if nums[left] == target:
                left_found = True
            else:
                left += 1

            if nums[right] == target:
                right_found = True
            else:
                right -= 1

        return [left, right] if left_found and right_found else [-1, -1]


def main():
    solution = Solution()
    print(solution.searchRange([5, 7, 8, 8, 8, 10], 8))


if __name__ == '__main__':
    main()

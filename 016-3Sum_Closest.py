class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first = 0
        last = len(nums) - 1
        if last < 2:
            return []
        temp_nums = sorted(nums)
        min_diff = temp_nums[0] + temp_nums[1] + temp_nums[last] - target
        while first < last - 1:
            second = first + 1
            while second < last:
                diff = temp_nums[first] + temp_nums[second] + temp_nums[last] - target
                if diff > 0:
                    last -= 1
                elif diff < 0:
                    second += 1
                else:
                    min_diff = 0
                    break
                if abs(min_diff) > abs(diff):
                    min_diff = diff

            first += 1
            last = len(temp_nums) - 1
        return min_diff + target


def main():
    # l = [1, 1, 1, 0]
    l = [-1, 2, 1, -4]
    # target = 100
    target = 1
    solution = Solution()
    print(solution.threeSumClosest(l, target))


if __name__ == '__main__':
    main()

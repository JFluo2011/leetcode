class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        first = 0
        last = len(nums) - 1
        if last < 2:
            return []
        res_list = []
        temp_nums = sorted(nums)
        while (first < last - 1) and last >= 2:
            second = first + 1
            while second < last:
                if temp_nums[first] + temp_nums[second] + temp_nums[last] > 0:
                    last -= 1
                elif temp_nums[first] + temp_nums[second] + temp_nums[last] < 0:
                    second += 1
                else:
                    res_list.append((temp_nums[first], temp_nums[second], temp_nums[last]))
                    second += 1
                    last -= 1
            first += 1
            last = len(nums) - 1
        return [list(i) for i in list(set(res_list))]


def main():
    l = [1, -1]
    solution = Solution()
    print(solution.threeSum(l))


if __name__ == '__main__':
    main()

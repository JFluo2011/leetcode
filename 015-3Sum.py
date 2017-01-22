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

    def better(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        results = []
        v_pre1 = 0
        found = False
        for index1, value1 in enumerate(nums):
            d = dict()
            if index1 == 0:
                v_pre1 = value1
            else:
                if value1 == v_pre1:
                    continue
                v_pre1 = value1
            v_pre2 = 0
            for index2, value2 in enumerate(nums[index1 + 1:]):
                index2 = index1 + 1
                if index2 == index1 + 1:
                    v_pre2 = value2
                else:
                    if found and value2 == v_pre2:
                        continue
                    v_pre2 = value2
                diff = -value1 - value2
                if diff in d:
                    results.append((value1, diff, value2))
                    found = True
                    continue
                found = False
                d[value2] = index2

        return results

    def better2(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        results = []
        found = False
        length = len(nums)
        for index1 in range(length):
            d = dict()
            if index1 != 0:
                if nums[index1] == nums[index1-1]:
                    continue
            for index2 in range(index1+1, length):
                if index2 != index1 + 1:
                    if found and nums[index2-1] == nums[index2]:
                        continue
                diff = -nums[index1] - nums[index2]
                if diff in d:
                    results.append((nums[index1], diff, nums[index2]))
                    found = True
                    continue
                found = False
                d[nums[index2]] = index2

        return results


def main():
    args = [
        # [],
        # [0, 0],
        # [1, -1],
        # [-1, 0, 1],
        # [0, 0, 0, 0],
        # [1, 2, -2, -1],
        # [-1, -1, -1, 2, 2],
        [3, 0, -2, -1, 1, 2],
        # [-1, 0, 1, 2, -1, -4],
        [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0],
    ]
    solution = Solution()
    for arg in args:
        print("***********************************")
        print(arg)
        print("solution1: {}".format(solution.threeSum(arg)))
        print("solution2: {}".format(solution.better(arg)))
        print("solution3: {}".format(solution.better2(arg)))
        print("***********************************")


if __name__ == '__main__':
    main()

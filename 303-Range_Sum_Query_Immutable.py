class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        from collections import defaultdict
        self.sums = defaultdict(int)
        sums = 0
        for i, num in enumerate(nums):
            sums += num
            self.sums[i] = sums

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        if i > j:
            return 0

        return self.sums[j] - self.sums[i-1]


def main():
    # Your NumArray object will be instantiated and called as such:
    nums = [-2, 0, 3, -5, 2, -1]
    num_array = NumArray(nums)
    print(num_array.sumRange(0, 2))
    print(num_array.sumRange(2, 5))
    print(num_array.sumRange(0, 5))


if __name__ == '__main__':
    main()

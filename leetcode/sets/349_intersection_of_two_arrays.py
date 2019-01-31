class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1).intersection(nums2))


def main():
    args = [
        ([], []),
        ([], [1]),
        ([1, 2, 2, 1], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4])
    ]
    s = Solution()
    for num1, num2 in args:
        print(s.intersection(num1, num2))


if __name__ == '__main__':
    main()

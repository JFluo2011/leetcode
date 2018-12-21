class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l = sorted(nums1 + nums2)
        length = len(l)
        return l[(length - 1)/2] if length % 2 != 0 else (l[length/2 - 1] + l[length/2])/2.0
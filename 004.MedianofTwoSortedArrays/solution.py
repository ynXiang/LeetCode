class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        length = len(nums1)
        if length/2*2 == length:
            return float((nums1[length/2-1]) + nums1[length/2]) / 2
        else:
            return nums1[int(length/2)]
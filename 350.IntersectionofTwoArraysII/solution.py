class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        return self.inter(nums1, nums2)
        
    def inter(self, nums1, nums2):
        if not len(nums1) or not len(nums2):
            return []
        elif nums1[0] == nums2[0]:
            return [nums1[0]] + self.inter(nums1[1:], nums2[1:])
        elif nums1[0] < nums2[0]:
            return self.inter(nums1[1:], nums2)
        elif nums1[0] > nums2[0]:
            return self.inter(nums1, nums2[1:])

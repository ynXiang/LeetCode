class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1, d2 = {}, {}
        for num in nums1:
            if num not in d1:
                d1[num] = 1
            else:
                d1[num] += 1
        for num in nums2:
            if num not in d2:
                d2[num] = 1
            else:
                d2[num] += 1
        res = []
        for num, cnt in d1.items():
            if num in d2:
                res.extend([num]*min(cnt, d2[num]))
        return res

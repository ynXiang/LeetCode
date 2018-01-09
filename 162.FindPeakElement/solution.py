class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums) - 1
        while i < j:
            k = (i + j) // 2
            if k > 0 and nums[k-1] > nums[k]:
                j = k - 1
            elif k < len(nums) - 1 and nums[k] < nums[k+1]:
                i = k + 1
            else:
                return k
        return (i + j) // 2

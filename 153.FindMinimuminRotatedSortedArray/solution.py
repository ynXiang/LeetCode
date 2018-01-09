class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, len(nums)-1
        while i < j:
            if nums[i] < nums[j]:
                return nums[i]
            k = (i + j) // 2
            if nums[k] >= nums[i]:
                i = k + 1
            else:
                j = k
        return nums[i]

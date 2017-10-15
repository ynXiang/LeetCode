class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        i, j = 0, len(nums)-1
        k = (i+j) / 2
        while i < j:
            if target == nums[k]:
                break
            elif target > nums[k]:
                i = k + 1
                k = (i+j) / 2
            else:
                j = k - 1
                k = (i+j) / 2
        if target != nums[k]:
            return [-1, -1]
        i = j = k
        while i >= 0 and nums[i] == target:
            i -= 1
        while j < len(nums) and nums[j] == target:
            j += 1
        return [i+1, j-1]

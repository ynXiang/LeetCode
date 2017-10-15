class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        i = j = 0
        while j < len(nums):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1
        j = i
        while j < len(nums):
            if nums[j] == 1:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
            j += 1

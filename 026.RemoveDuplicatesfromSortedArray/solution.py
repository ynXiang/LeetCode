class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i, j = 0, 0
        while j < len(nums):
            if j == 0 or nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i

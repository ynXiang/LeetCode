class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        i = 0
        while i < len(nums):
            if i == len(nums) - z:
                break
            elif nums[i] == 0:
                nums[:] = nums[:i] + nums[i+1:] + [0]
                z += 1
            else:
                i += 1

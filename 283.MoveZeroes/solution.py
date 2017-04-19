class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        for i in range(len(nums)):
            if i == len(nums) - z + 1:
                break
            if nums[i] == 0:
                nums = nums[:i] + nums[i+1:] + [0]
                z += 1
            i -= 1
        print nums
        return

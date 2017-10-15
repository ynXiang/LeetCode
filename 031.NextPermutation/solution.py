class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        
        """
        if len(nums) <= 1:
            return 
        index = -1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i-1
                break
        if index == -1:
            nums.sort()
        else:
            index_m, m = index+1, nums[index+1]
            for i in range(len(nums[index+1:])):
                if nums[index+1+i] > nums[index] and nums[index+1+i] < m:
                    index_m, m = index+1+i, nums[index+1+i]
            nums[index], nums[index_m] = nums[index_m], nums[index]
            nums[:] = nums[:index+1] + sorted(nums[index+1:])
        return

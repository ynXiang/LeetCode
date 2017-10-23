import copy

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        targetDict = {}
        for i in xrange(len(nums)):
            if nums[i] in targetDict:
                return [targetDict[nums[i]], i]
            else:
                targetDict[target-nums[i]] = i

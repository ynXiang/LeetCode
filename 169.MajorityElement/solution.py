import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = math.floor(len(nums)/2)
        ele = {}
        for i in range(len(nums)):
            if nums[i] not in ele:
                ele[nums[i]] = 1
            else:
                ele[nums[i]] += 1
        majority = sorted(ele.items(), key=lambda d:d[1], reverse=True)[0][0]
        return majority

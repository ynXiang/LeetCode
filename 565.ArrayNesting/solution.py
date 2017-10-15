import random

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxLen = 0
        remain = len(nums)
        while maxLen < remain:
            p = random.randint(0, len(nums)-1)
            while nums[p] < 0:
                p = random.randint(0, len(nums)-1)
            curLen = 0
            while nums[p] >= 0:
                curLen += 1
                tmp, nums[p] = nums[p], -1
                p = tmp
            nums[p] = -1
            remain -= curLen
            if curLen > maxLen:
                maxLen = curLen
        return maxLen

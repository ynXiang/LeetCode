class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxPos = 0
        curPos = 0
        while curPos <= maxPos:
            maxPos = max(maxPos, nums[curPos]+curPos)
            if maxPos >= len(nums) - 1:
                return True
            curPos += 1
        return False

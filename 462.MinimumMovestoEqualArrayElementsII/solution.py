class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        target = nums[len(nums)/2]
        count = 0
        for v in nums:
            count += abs(v - target)
        return count

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        sum = 0
        i = 0
        while i < len(nums):
            sum += nums[i]
            i += 2
        return sum

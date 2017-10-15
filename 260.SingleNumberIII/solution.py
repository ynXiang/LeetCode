class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        x = 0
        for v in nums:
            x ^= v
        num1 = num2 = 0
        bit = x & ~(x-1)
        for v in nums:
            if v & bit > 0:
                num1 ^= v
            else:
                num2 ^= v
        return num1, num2

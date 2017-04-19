class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        length = 0
        for num in nums:
            if num == 1:
                length += 1
            else:
                if length > max_length:
                    max_length = length
                length = 0
        return max(max_length, length)

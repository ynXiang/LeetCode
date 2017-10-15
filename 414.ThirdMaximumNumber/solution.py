class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniqueNums = list(sorted(set(nums)))
        if len(uniqueNums) < 3:
            return uniqueNums[-1]
        else:
            return uniqueNums[-3]

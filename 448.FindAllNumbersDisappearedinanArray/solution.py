class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.sort()
        i = 1
        ans = list()
        for num in nums:
            if num == i:
                i += 1
            elif num > i:
                ans += list(range(i, num))
                i = num + 1
        ans += list(range(i, len(nums)+1))
        return ans

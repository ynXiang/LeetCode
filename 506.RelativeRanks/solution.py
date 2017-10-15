#https://discuss.leetcode.com/topic/77943/python-solution

import copy

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        originNums = copy.deepcopy(nums)
        for i in range(len(originNums)):
            originNums[i] = (originNums[i], i)
        originNums.sort(reverse = True)
        switcher = {
            0: "Gold Medal",
            1: "Silver Medal",
            2: "Bronze Medal"
        }
        for i in range(len(originNums)):
            nums[originNums[i][1]] = switcher.get(i, str(i+1))
        return nums

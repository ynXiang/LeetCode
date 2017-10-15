#https://discuss.leetcode.com/topic/17199/python-solution-3-lines

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = [[v] for v in nums]
        for i in reversed(range(len(nums)-1)):
            for j in range(i+1, len(nums)):
                if j == i+1:
                    l[i].append(max(nums[i],nums[j]))
                else:
                    l[i].append(max([l[i][k-1-i]+l[k+1][-1] for k in range(i+1,j)] + [l[i+1][j-i-1], l[i][j-i-1]]))
                    print i,j, l
        return l[0][-1]

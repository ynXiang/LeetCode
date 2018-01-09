#https://discuss.leetcode.com/topic/34467/pretty-short-c-java-ruby-python

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        i, j, k = 0, len(nums), 0
        while i < j:
            k = (i + j) // 2
            if nums[k] == target:
                return k
            elif (nums[0] <= target) ^ (target < nums[k]) ^ (nums[k] < nums[0]):
                i = k + 1
            else:
                j = k
        return -1

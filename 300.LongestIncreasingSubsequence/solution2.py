#https://discuss.leetcode.com/topic/28738/java-python-binary-search-o-nlogn-time-with-explanation
#O(nlogn)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tails = [0 for i in range(len(nums))]
        size = 0
        for num in nums:
            i, j = 0, size
            k = (i + j) // 2
            while i < j:
                if tails[k] < num:
                    i = k + 1
                elif tails[k] > num:
                    j = k
                else:
                    break
                k = (i + j) // 2
            tails[k] = num
            size = max(size, k+1)
        return size

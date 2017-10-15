class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        maximum = 0
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        k = sorted(d.keys())
        for i in range(len(k)-1):
            if abs(k[i] - k[i+1]) == 1 and d[k[i]] + d[k[i+1]] > maximum:
                maximum = d[k[i]] + d[k[i+1]]
        return maximum

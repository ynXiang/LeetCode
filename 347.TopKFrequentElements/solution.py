class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        s = sorted(d.items(), key=lambda x:x[1], reverse=True)
        return [s[i][0] for i in range(k)]

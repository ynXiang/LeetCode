class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0
        ans = 0
        d = {}
        for v in nums:
            if v not in d:
                d[v] = 1
            else:
                d[v] += 1
        if k == 0:
            for v in d.values():
                if v > 1:
                    ans += 1
            return ans
        else:
            s = sorted(d.keys())
            for i,v in enumerate(s):
                if v+k in s[i+1:]:
                    ans += 1
            return ans

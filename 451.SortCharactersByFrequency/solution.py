class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d = {}
        for c in s:
            if c not in d:
                d[c] = 1
            else:
                d[c] += 1
        ans = ""
        for k,v in sorted(d.items(), key=lambda x:x[1], reverse=True):
            ans += k * v
        return ans

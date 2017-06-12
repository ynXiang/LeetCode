class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ans = []
        if len(s) < len(p):
            return []
        pd = {}
        for t in p:
            if t not in pd:
                pd[t] = 1
            else:
                pd[t] += 1
        sd = {}
        for t in s[:len(p)]:
            if t not in sd:
                sd[t] = 1
            else:
                sd[t] += 1
        if sd == pd:
            ans.append(0)
        for i in range(1, len(s)-len(p)+1):
            if s[i-1] != s[i+len(p)-1]:
                if s[i+len(p)-1] not in sd:
                    sd[s[i+len(p)-1]] = 1
                else:
                    sd[s[i+len(p)-1]] += 1
                if sd[s[i-1]] == 1:
                    del sd[s[i-1]]
                else:
                    sd[s[i-1]] -= 1
            if sd == pd:
                ans.append(i)
        return ans

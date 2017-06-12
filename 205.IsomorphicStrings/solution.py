class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd = {}
        for i,v in enumerate(s):
            if v not in sd:
                sd[v] = [i]
            else:
                sd[v].append(i)
        td = {}
        for i,v in enumerate(t):
            if v not in td:
                td[v] = [i]
            else:
                td[v].append(i)
        return sorted(sd.values()) == sorted(td.values())

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pd = {}
        for i,v in enumerate(pattern):
            if v not in pd:
                pd[v] = [i]
            else:
                pd[v].append(i)
        strl = str.strip().split(" ")
        sd = {}
        for i,v in enumerate(strl):
            if v not in sd:
                sd[v] = [i]
            else:
                sd[v].append(i)
        return sorted(pd.values()) == sorted(sd.values())

import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        D = dict(collections.Counter(t))
        newS = [i for i in enumerate(s) if i[1] in D]
        init = cur = 0
        min_l = len(s)
        find = False
        for v in newS:
            D[v[1]] -= 1
            while not [i for i in D.values() if i > 0]:
                find = True
                if min_l > v[0] - newS[cur][0] + 1:
                    min_l = v[0] - newS[cur][0] + 1
                    init = newS[cur][0]
                D[newS[cur][1]] += 1
                cur += 1
        return ('', s[init:init+min_l])[find]

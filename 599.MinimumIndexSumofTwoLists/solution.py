class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i,v in enumerate(list1):
            d[v] = [True, i]
        for i,v in enumerate(list2):
            if v in d:
                d[v] = [False, d[v][1]+i]
        ans = []
        l = sorted(d.items(), key=lambda x:x[1])
        minimum = l[0][1][1]
        for k,v in l:
            if not v[0] and v[1] == minimum:
                ans.append(k)
            else:
                break
        return ans

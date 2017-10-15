class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}
        for v in people:
            if v[1] not in d:
                d[v[1]] = [v[0]]
            else:
                d[v[1]].append(v[0])
        ans = []
        for k,v in sorted(d.items()):
            if k == 0:
                ans += [[i,0] for i in sorted(d[k])]
            else:
                for i in sorted(d[k], reverse=True):
                    count = 0
                    for index,value in enumerate(ans):
                        if value[0] >= i:
                            count += 1
                        if count == k:
                            ans.insert(index+1, [i,k])
                            break
        return ans

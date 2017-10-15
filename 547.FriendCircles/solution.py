class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        gs = [-1] * len(M)
        count = 0
        for i in range(len(M)):
            g = []
            for j in range(i):
                if M[i][j] == 1 and gs[j] not in g:
                    g.append(gs[j])
            if not g:
                gs[i] = i
                count += 1
            else:
                g.sort()
                gs[i] = g[0]
                count -= len(g) - 1
                for k in range(len(gs[:i])):
                    if gs[k] in g[1:]:
                        gs[k] = g[0]
        return count

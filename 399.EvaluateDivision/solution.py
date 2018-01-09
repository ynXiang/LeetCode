class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        d = {}
        for i in range(len(equations)):
            x, y = equations[i]
            if x not in d and y not in d:
                d[x] = (y, values[i])
                d[y] = (y, 1)
            elif x not in d:
                d[x] = (y, values[i])
            elif y not in d:
                d[y] = (x, 1/values[i])
            else:
                curX, curY = x, y
                v1, v2 = 1, 1
                while d[curX][0] != curX:
                    v1 *= d[curX][1]
                    curX = d[curX][0]
                while d[curY][0] != curY:
                    v2 *= d[curY][1]
                    curY = d[curY][0]
                d[curX] = (curY, values[i]*v2/v1)
        res = [0 for _ in range(len(queries))]
        for i in range(len(queries)):
            x, y = queries[i]
            if x not in d or y not in d:
                res[i] = -1.0
            else:
                curX, curY = x, y
                v1, v2 = 1, 1
                while d[curX][0] != curX:
                    v1 *= d[curX][1]
                    curX = d[curX][0]
                while d[curY][0] != curY:
                    v2 *= d[curY][1]
                    curY = d[curY][0]
                if curX != curY:
                    res[i] = -1.0
                else:
                    res[i] = v1/v2
        return res

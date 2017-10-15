class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m * n
        mm = ops[0][0]
        nm = ops[0][1]
        for v in ops[1:]:
            if v[0] < mm:
                mm = v[0]
            if v[1] < nm:
                nm = v[1]
        return mm * nm

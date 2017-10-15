class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = ["()"]
        for i in range(n-1):
            tmp = []
            for j in ans:
                for k in range(len(j)+1):
                    tmp.append(j[:k]+"()"+j[k:])
            ans = list(set(tmp))
        return ans

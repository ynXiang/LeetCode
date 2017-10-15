class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        L = [i+1 for i in range(N)]
        return self.countArrangementHelp(N, L)
    
    def countArrangementHelp(self, N, L):
        if N <= 0:
            return 1
        else:
            ans = 0
            for i in range(N):
                if L[i] % N == 0 or N % L[i] == 0:
                    L[i], L[-1] = L[-1], L[i]
                    ans += self.countArrangementHelp(N-1, L[:-1])
                    L[i], L[-1] = L[-1], L[i]
            return ans

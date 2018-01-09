class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        next = [0 for i in xrange(len(B))]
        j, k = 0, -1
        next[0] = -1
        while j+1 < len(B):
            if (k == -1 or B[j] == B[k]):
                j += 1
                k += 1
                next[j] = k if (B[j] != B[k]) else next[k]
            else:
                k = next[k]
        i, j = 0, 0
        while i < len(A):
            while j < len(B) and A[(i+j)%len(A)] == B[j]:
                j += 1
            if j == len(B):
                return -(-(i+j) // len(A))
            i += max(j - next[j], 1)
            j = max(next[j], 0)
        return -1

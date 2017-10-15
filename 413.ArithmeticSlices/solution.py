class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        ans = 0
        count = self.getArithmeticSlicesLength(A)
        for l in count:
            ans += (l-1) * (l-2) / 2
        return ans
        
    def getArithmeticSlicesLength(self, A):
        if len(A) < 3:
            return []
        i = 2
        count = []
        diff = A[1] - A[0]
        length = 2
        while i < len(A):
            if A[i] - A[i-1] == diff:
                length += 1
            else:
                diff = A[i] - A[i-1]
                if length > 2:
                    count.append(length)
                    length = 2
            i += 1
        if length > 2:
            count.append(length)
        return count
            

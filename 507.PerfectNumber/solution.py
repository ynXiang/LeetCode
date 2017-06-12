import math

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1:
            return False
        return num == sum(self.findFactors(num))
        
    def findFactors(self, num):
        ans = [1]
        for i in range(2, int(math.sqrt(num))+1):
            if num % i == 0:
                ans.extend([i, num/i])
        return ans

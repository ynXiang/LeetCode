import math

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num^(2**int(math.log(num,2)+1)-1)

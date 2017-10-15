import math

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num == 0:
            return [0]
        p = int(math.log(num, 2))
        diff = int(num - 2**p)
        ans = [0, 1]
        while p > 0:
            ans += [i+1 for i in ans] if p != 1 else [i+1 for i in ans[:diff+1]]
            p -= 1
        return ans

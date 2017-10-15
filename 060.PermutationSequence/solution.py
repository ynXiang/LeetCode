class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = ""
        nums = [i+1 for i in range(n)]
        numOfPermutations = 1
        for i in range(n-1):
            numOfPermutations *= i + 1
        i = n - 1
        k -= 1
        while i > 0:
            res += str(nums[k // numOfPermutations])
            del nums[k // numOfPermutations]
            k %= numOfPermutations
            numOfPermutations /= i
            i -= 1
        res += str(nums[0])
        return res

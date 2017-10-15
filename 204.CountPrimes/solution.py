#https://discuss.leetcode.com/topic/14036/fast-python-solution/4

import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        count = 1
        primes = []
        i = 3
        while i < n:
            isPrime = True
            for p in primes:
                if i % p == 0:
                    isPrime = False
                    break
            if isPrime:
                count += 1
                if i <= int(math.sqrt(n)):
                    primes.append(i)
            i += 2
        return count

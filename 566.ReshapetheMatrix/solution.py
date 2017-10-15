#https://discuss.leetcode.com/topic/87899/python-solutions

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m, n = len(nums), len(nums[0])
        if m * n == r * c:
            ans = [[0 for j in range(c)] for i in range(r)]
            for i in range(r):
                for j in range(c):
                    s = i * c + j
                    p, q = int(s / n), s % n
                    ans[i][j] = nums[p][q]
            return ans
        else:
            return nums

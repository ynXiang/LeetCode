class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return self.helper(candidates[::-1], 0, target)
        
    def helper(self, candidates, index, target):
        res = []
        for i in range(index, len(candidates)):
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                res += [[candidates[i]]]
            else:
                res += [rest + [candidates[i]] for rest in self.helper(candidates, i, target-candidates[i])]
        return res

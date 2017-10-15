class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        l = [""]
        chars = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        for i in digits:
            char = chars[int(i)-2]
            l = [m+n for m in l for n in char]
        return l


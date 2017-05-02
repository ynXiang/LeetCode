class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict = {}
        for i in s:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        for i in t:
            if i not in dict:
                return False
            else:
                dict[i] -= 1
        return len(dict.items()) == 0 or max(dict.values()) == 0 and min(dict.values()) == 0

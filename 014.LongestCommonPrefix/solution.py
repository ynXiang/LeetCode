class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        ans = strs[0]
        for string in strs[1:]:
            for i in range(len(ans)):
                if i == len(string) or ans[i] != string[i]:
                    ans = ans[:i]
                    break
            if ans == "":
                return ""
        return ans

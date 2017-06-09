class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = s.strip().split(" ")
        count = 0
        for i in l:
            if i != "":
                count += 1
        return count

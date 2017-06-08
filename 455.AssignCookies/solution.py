class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        j = 0
        for i in g:
            if j == len(s):
                break
            while i > s[j]:
                j += 1
                if j == len(s):
                    return count
            count += 1
            j += 1
        return count

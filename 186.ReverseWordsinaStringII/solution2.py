class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        def reverse(s, e):
            while s < e:
                str[s], str[e] = str[e], str[s]
                s += 1
                e -= 1
        reverse(0, len(str)-1)
        i = j = 0
        while j < len(str):
            while j < len(str) and str[j] != ' ':
                j += 1
            reverse(i, j-1)
            j = j + 1
            i = j

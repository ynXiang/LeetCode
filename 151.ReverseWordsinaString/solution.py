class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == '':
            return ''
        i, storeIndex = 0, 0
        l = list(s)[::-1]
        while i < len(l):
            j = i
            while j < len(l) and l[j] != ' ':
                j += 1
            l[storeIndex:storeIndex+j-i] = l[i:j][::-1]
            storeIndex += j-i+1
            if storeIndex >= len(l):
                storeIndex -= 1
                break
            l[storeIndex-1] = ' '
            while j < len(l) and l[j] == ' ':
                j += 1
            i = j
        startIndex = 0 if l[0] != ' ' else 1
        storeIndex -= 1 if l[storeIndex-1] == ' ' else 0
        return ''.join(l[startIndex:storeIndex])

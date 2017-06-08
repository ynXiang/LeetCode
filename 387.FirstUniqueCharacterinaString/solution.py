class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash = {}
        for i in range(26):
            hash[i] = 0
        for i in s:
            hash[ord(i)-97] += 1
        index = -1
        for i in hash:
            if hash[i] == 1 and (index == -1 or s.index(chr(i+97)) < index):
                index = s.index(chr(i+97))
        return index

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash = {}
        for i in range(26):
            hash[i] = 0
        for i in magazine:
            hash[ord(i)-97] += 1
        for i in ransomNote:
            hash[ord(i)-97] -= 1
            if hash[ord(i)-97] < 0:
                return False
        return True

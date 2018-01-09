class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Map, s2Map = {chr(c+97):0 for c in range(26)}, {chr(c+97):0 for c in range(26)}
        l1 = len(s1)
        for c in s1:
            s1Map[c] += 1
        for c in s2[:l1]:
            s2Map[c] += 1
        if s1Map == s2Map:
            return True
        for i in range(len(s2)-l1):
            s2Map[s2[i]] -= 1
            s2Map[s2[i+l1]] += 1
            if s1Map == s2Map:
                return True
        return Falseclass Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        s1Map, s2Map = {chr(c+97):0 for c in range(26)}, {chr(c+97):0 for c in range(26)}
        l1 = len(s1)
        for c in s1:
            s1Map[c] += 1
        for c in s2[:l1]:
            s2Map[c] += 1
        if s1Map == s2Map:
            return True
        for i in range(len(s2)-l1):
            s2Map[s2[i]] -= 1
            s2Map[s2[i+l1]] += 1
            if s1Map == s2Map:
                return True
        return False

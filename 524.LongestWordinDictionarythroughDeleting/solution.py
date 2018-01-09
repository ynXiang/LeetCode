class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        maxL = 0
        maxWord = ''
        for word in d:
            if len(word) < maxL:
                continue
            i, j = 0, 0
            while i < len(s) and j < len(word):
                if s[i] == word[j]:
                    j += 1
                i += 1
            if j == len(word) and (maxL < len(word) or maxL == len(word) and word < maxWord):
                maxL, maxWord = len(word), word
        return maxWord

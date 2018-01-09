class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key=lambda x:(-len(x),x))
        for word in d:
            if len(word) > len(s):
                continue
            index = 0
            for c in word:
                index = s.find(c, index)
                if index == -1:
                    break
                index += 1
            if index != -1:
                return word
        return ''

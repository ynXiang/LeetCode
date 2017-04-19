class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        L = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        for word in words:
            if word[0].lower() in L[0]:
                line = 0
            elif word[0].lower() in L[1]:
                line = 1
            elif word[0].lower() in L[2]:
                line = 2
            i = 1
            for char in word[1:].lower():
                if char not in L[line]:
                    break
                i += 1
            if i == len(word):
                ans.append(word)
        return ans

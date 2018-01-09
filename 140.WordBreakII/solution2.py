class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict: return []
        words = set(wordDict)
        lens = set(len(word) for word in wordDict)
        self.dict = {0: ['']}
        def search(i):
            if i not in self.dict:
                self.dict[i] = [rest + (rest and ' ') + s[i - span: i] 
                            for span in lens if s[i - span: i] in wordDict for rest in search(i - span)]
            return self.dict[i]
        return search(len(s))

class TrieNode(object):
    def __init__(self):
        self.children = {}

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def find(i):
            cur = trie
            res = []
            j = i
            while j < len(s) and s[j] in cur.children:
                cur = cur.children[s[j]]
                j += 1
                if '#' in cur.children:
                    if j == len(s):
                        res += [s[i:j]]
                    else:
                        res += [s[i:j] + ' ' + rest for rest in restWords[j]]
            restWords[i] = res
        trie = TrieNode()
        restWords = [[] for i in xrange(len(s))]
        for word in wordDict:
            cur = trie
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.children['#'] = None
        for i in xrange(len(s)-1, -1, -1):
            find(i)
        return restWords[0]

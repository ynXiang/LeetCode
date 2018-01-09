class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        d = {}
        for pair in pairs:
            if pair[0] in d and pair[1] not in d:
                d[pair[0]].add(pair[1])
                d[pair[1]] = d[pair[0]]
            elif pair[0] not in d and pair[1] in d:
                d[pair[1]].add(pair[0])
                d[pair[0]] = d[pair[1]]
            elif pair[0] not in d and pair[1] not in d:
                d[pair[0]] = set(pair)
                d[pair[1]] = d[pair[0]]
            else:
                d[pair[0]] |= d[pair[1]]
                for i in d[pair[1]]:
                    d[i] = d[pair[0]]
        for i in xrange(len(words1)):
            if words1[i] != words2[i] and (words1[i] not in d or words2[i] not in d[words1[i]]):
                return False
        return True

#https://discuss.leetcode.com/topic/3297/2-line-python-solution-ac-with-350ms-some-useful-python-tricks
#https://discuss.leetcode.com/topic/45639/java-beat-100-use-prime-number

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        mapStrs = {}
        for string in strs:
            mapCharacters = {}
            for character in sorted(string):
                mapCharacters[character] = mapCharacters.get(character, 0) + 1
            if tuple(mapCharacters.items()) in mapStrs:
                mapStrs[tuple(mapCharacters.items())].append(string)
            else:
                mapStrs[tuple(mapCharacters.items())] = [string]
        return list(mapStrs.values())

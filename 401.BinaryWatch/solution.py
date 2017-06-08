class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        ans = []
        for i in range(min(num+1, 5)):
            hrs = self.combination(i, [1,2,4,8])
            mins = self.combination(num-i, [1,2,4,8,16,32])
            strhrs = []
            strmins = []
            for i in hrs:
                if i < 12:
                    strhrs.append(str(i))
            for i in mins:
                if i < 60:
                    strmins.append("0"+str(i) if i < 10 else str(i))
            ans += [i+":"+j for i in strhrs for j in strmins]
        return sorted(ans)
        
    def combination(self, m, l):
        return list(set([i+j for i in l for j in self.combination(m-1, list(set(l)-set([i])))])) if m > 0 else [0]

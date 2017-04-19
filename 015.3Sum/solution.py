class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = list()
        nums.sort()
        zeros = nums.count(0)
        zexist = True
        neg = list()
        pos = list()
        if zeros >= 3:
            ans.append([0, 0, 0])
        elif zeros == 0:
            zexist = False
        if zexist:
            neg = nums[:nums.index(0)]
            pos = nums[nums.index(0)+zeros:]
            pre = None
            for _ in neg:
                if _ == pre:
                    continue
                else:
                    pre = _
                if -_ in pos:
                    ans.append([_,0,-_])
        else:
            for _ in nums:
                if _ > 0:
                    neg = nums[:nums.index(_)]
                    pos = nums[nums.index(_):]
                    break
        for i in range(len(neg)):
            for j in range(i+1, len(neg)):
                if -neg[i]-neg[j] in pos and [neg[i],neg[j],-neg[i]-neg[j]] not in ans:
                    ans.append([neg[i],neg[j],-neg[i]-neg[j]])
        for i in range(len(pos)):
            for j in range(i+1, len(pos)):
                if -pos[i]-pos[j] in neg and [-pos[i]-pos[j],pos[i],pos[j]] not in ans:
                    ans.append([-pos[i]-pos[j],pos[i],pos[j]])     
        return ans
                

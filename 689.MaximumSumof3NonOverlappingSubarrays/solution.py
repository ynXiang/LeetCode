class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 3 * k:
            return []
        kSum = sum(nums[:k])
        sumList = [kSum]
        for i in range(1, len(nums)-k+1):
            kSum += nums[i+k-1] - nums[i-1]
            sumList.append(kSum)
        lToRMaxList = [(0, 0)]
        rToLMaxList = [(0, 0)]
        for i in range(len(sumList)-2*k):
            if lToRMaxList[-1][0] < sumList[i]:
                lToRMaxList.append((sumList[i], i))
            else:
                lToRMaxList.append(lToRMaxList[-1])
            if rToLMaxList[-1][0] < sumList[-i-1]:
                rToLMaxList.append((sumList[-i-1], len(nums)-k-i))
            else:
                rToLMaxList.append(rToLMaxList[-1])
        maxRes, res = 0, []
        for i in range(len(sumList)-k*2):
            if maxRes < lToRMaxList[i+1][0] + sumList[i+k] + rToLMaxList[-i-1][0]:
                maxRes = lToRMaxList[i+1][0] + sumList[i+k] + rToLMaxList[-i-1][0]
                res = [lToRMaxList[i+1][1], i+k, rToLMaxList[-i-1][1]]
        return resclass Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < 3 * k:
            return []
        kSum = sum(nums[:k])
        sumList = [kSum]
        for i in range(1, len(nums)-k+1):
            kSum += nums[i+k-1] - nums[i-1]
            sumList.append(kSum)
        lToRMaxList = [(0, 0)]
        rToLMaxList = [(0, 0)]
        for i in range(len(sumList)-2*k):
            if lToRMaxList[-1][0] < sumList[i]:
                lToRMaxList.append((sumList[i], i))
            else:
                lToRMaxList.append(lToRMaxList[-1])
            if rToLMaxList[-1][0] < sumList[-i-1]:
                rToLMaxList.append((sumList[-i-1], len(nums)-k-i))
            else:
                rToLMaxList.append(rToLMaxList[-1])
        maxRes, res = 0, []
        for i in range(len(sumList)-k*2):
            if maxRes < lToRMaxList[i+1][0] + sumList[i+k] + rToLMaxList[-i-1][0]:
                maxRes = lToRMaxList[i+1][0] + sumList[i+k] + rToLMaxList[-i-1][0]
                res = [lToRMaxList[i+1][1], i+k, rToLMaxList[-i-1][1]]
        return res

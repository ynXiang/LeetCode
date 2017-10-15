class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        nums2 = nums + nums
        i, j = 0, len(nums2)-1
        k = (i+j) / 2
        middle = nums2[k]
        direction = 0 if target < middle else 1
        while i < j:
            if target == nums2[k]:
                return k % len(nums)
            elif not direction and (nums2[k] >= middle or target > nums2[k]) or direction and target > nums2[k] and nums2[k] >= middle:
                print 'A',i,j,k,direction
                i = k + 1
                k = (i+j) / 2
            elif not direction and target < nums2[k] and nums2[k] <= middle or direction and (nums2[k] <= middle or target < nums2[k]):
                print 'B',i,j,k,direction
                j = k - 1
                k = (i+j) / 2
        return k % len(nums) if target == nums2[k] else -1

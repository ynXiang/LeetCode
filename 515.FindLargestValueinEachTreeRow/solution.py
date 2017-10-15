# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rows = self.getRows(root)
        ans = []
        for l in rows:
            ans.append(max(l))
        return ans
        
    def getRows(self, root):
        if not root:
            return []
        ll = self.getRows(root.left)
        rl = self.getRows(root.right)
        if len(ll) > len(rl):
            ll, rl = rl, ll
        l = [[root.val]]
        for i in range(len(ll)):
            l.append(ll[i] + rl[i])
        for i in range(len(ll), len(rl)):
            l.append(rl[i])
        return l

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        return self.tree(root, sum)[0]
        
    def tree(self, root, sum):
        if not root:
            return 0, {}
        lp, ld = self.tree(root.left, sum)
        rp, rd = self.tree(root.right, sum)
        d = {root.val:1}
        for k,v in ld.items():
            if k+root.val not in d:
                d[k+root.val] = v
            else:
                d[k+root.val] += v
        for k,v in rd.items():
            if k+root.val not in d:
                d[k+root.val] = v
            else:
                d[k+root.val] += v
        p = lp + rp
        if sum in d.keys():
            p += d[sum]
        return p, d

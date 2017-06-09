# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        d = self.count(root)
        newd = sorted(d.items(), key=lambda x:x[1], reverse=True)
        maximum = newd[0][1]
        ans = []
        for i in newd:
            if i[1] == maximum:
                ans.append(i[0])
        return ans
        
    def count(self, root):
        if not root:
            return {}
        d1 = self.count(root.left)
        d2 = self.count(root.right)
        d = {root.val:1}
        for k,v in d1.items():
            if k not in d:
                d[k] = v
            else:
                d[k] += v
        for k,v in d2.items():
            if k not in d:
                d[k] = v
            else:
                d[k] += v
        return d

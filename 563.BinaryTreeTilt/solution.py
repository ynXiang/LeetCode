# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.tiltWithSum(root)[0]
            
    def tiltWithSum(self, root):
        #return totel tilt of root and total sum of nodes including root
        if not root:
            return 0, 0
        elif not root.left and not root.right:
            return 0, root.val
        elif not root.left:
            t, s = self.tiltWithSum(root.right)
            return t + abs(s), s + root.val
        elif not root.right:
            t, s = self.tiltWithSum(root.left)
            return t + abs(s), s + root.val
        else:
            tl, sl = self.tiltWithSum(root.left)
            tr, sr = self.tiltWithSum(root.right)
            return tl + tr + abs(sl -sr), sl + sr + root.val

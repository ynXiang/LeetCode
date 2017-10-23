# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        if root:
            self.root = root
            self.left = BSTIterator(root.left)
            self.right = BSTIterator(root.right)
            self.cond = -1 if self.left.hasNext() else 0
        else:
            self.root = None
            self.left = None
            self.right = None
            self.cond = 2

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cond != 2

    def next(self):
        """
        :rtype: int
        """
        res = None
        if self.cond == -1:
            res = self.left.next()
            if not self.left.hasNext():
                self.cond = 0
        elif self.cond == 0:
            res = self.root.val
            self.cond = 1 if self.right.hasNext() else 2
        elif self.cond == 1:
            res = self.right.next()
            if not self.right.hasNext():
                self.cond = 2
        return res

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

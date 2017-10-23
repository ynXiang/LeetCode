#https://discuss.leetcode.com/topic/6575/my-solutions-in-3-languages-with-stack

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
        self.stack = []
        self.push(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.stack

    def next(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        self.push(res.right)
        return res.val

    def push(self, root):
        if root:
            self.stack.append(root)
            self.push(root.left)
                

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())

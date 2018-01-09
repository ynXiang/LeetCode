# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from Queue import *
        if not root:
            return []
        queue = Queue()
        queue.put(root)
        res = []
        reverse = False
        k = 1
        while queue.qsize():
            line = [0 for i in range(queue.qsize())]
            for i in range(queue.qsize()):
                cur = queue.get()
                if cur.left:
                    queue.put(cur.left)
                if cur.right:
                    queue.put(cur.right)
                index = -i-1 if reverse else i
                line[index] = cur.val
            res.append(line)
            reverse = not reverse
        return res

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return False
        queue = [root]
        while root.left:
            queue.append(root.left)
            root = root.left
        while k > 1 and queue:
            cur = queue.pop()
            if cur.right:
                queue.append(cur.right)
                cur = cur.right
                while cur.left:
                    queue.append(cur.left)
                    cur = cur.left
            k -= 1
        if k == 1:
            return queue[-1].val
        else:
            return None

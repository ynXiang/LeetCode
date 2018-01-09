# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        from Queue import *
        if not root:
            return
        queue = Queue()
        queue.put(root)
        while queue.qsize():
            last = None
            for i in range(queue.qsize()):
                cur = queue.get()
                if not cur: continue
                cur.next = last
                last = cur
                queue.put(cur.right)
                queue.put(cur.left)

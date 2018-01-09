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
        while root:
            cur = root
            next = None
            prev = None
            while cur:
                if cur.left:
                    if prev:
                        prev.next = cur.left
                    else:
                        next = cur.left
                    prev = cur.left
                if cur.right:
                    if prev:
                        prev.next = cur.right
                    else:
                        next = cur.right
                    prev = cur.right
                cur = cur.next
            root = next

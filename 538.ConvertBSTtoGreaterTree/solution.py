#https://discuss.leetcode.com/topic/83469/python-simple-with-explanation

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        valList = sorted(self.getValList(root))
        addList = [0]
        for v in valList[:0:-1]:
            addList = [v+addList[0]] + addList
        self.getGreaterTree(root, valList, addList)
        return root
        
    def getValList(self, root):
        if not root:
            return []
        else:
            return [root.val] + self.getValList(root.left) + self.getValList(root.right)
            
    def getGreaterTree(self, root, valList, addList):
        if not root:
            return
        else:
            root.val += addList[valList.index(root.val)]
            self.getGreaterTree(root.left, valList, addList)
            self.getGreaterTree(root.right, valList, addList)

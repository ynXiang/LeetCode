# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return self.deserializeHelper(data.split(','))
    
    def deserializeHelper(self, lData):
        if lData[0] == '':
            del lData[0]
            return None
        root = TreeNode(int(lData[0]))
        del lData[0]
        root.left = self.deserializeHelper(lData)
        root.right = self.deserializeHelper(lData)
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        d, _ = self.findFrequentTreeSumHelp(root)
        ans = []
        l = sorted(d.items(), key=lambda x:x[1], reverse=True)
        for k,v in l:
            if v == l[0][1]:
                ans.append(k)
            else:
                break
        return ans
    
    def findFrequentTreeSumHelp(self, root):
        if not root:
            return {}, 0
        else:
            ld, ls = self.findFrequentTreeSumHelp(root.left)
            rd, rs = self.findFrequentTreeSumHelp(root.right)
            d = ld
            for k,v in rd.items():
                if k not in d:
                    d[k] = v
                else:
                    d[k] += v
            rootSum = root.val + ls + rs
            if rootSum not in d:
                d[rootSum] = 1
            else:
                d[rootSum] += 1
            return d, rootSum

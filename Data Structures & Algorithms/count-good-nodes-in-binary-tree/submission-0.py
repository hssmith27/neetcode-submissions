# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def goodH(root, greatest):
            if not root:
                return 0
            maxVal = max(root.val, greatest)
            lAndR = goodH(root.left, maxVal) + goodH(root.right, maxVal)
            if root.val >= greatest:
                return 1 + lAndR
            return lAndR

        return goodH(root, -101)
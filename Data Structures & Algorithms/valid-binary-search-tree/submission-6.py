# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, minVal, maxVal):
            if not node:
                return True
            val = node.val
            if not (minVal < val and val < maxVal):
                return False
            return dfs(node.left, minVal, val) and dfs(node.right, val, maxVal)

        return dfs(root, float("-inf"), float("inf"))
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def dfs(node):
            if node is None:
                return False
            return isSubtreeH(node, subRoot) or dfs(node.left) or dfs(node.right)
            
        def isSubtreeH(big, sub):
            if not big and not sub:
                return True
            if (not big and sub) or (big and not sub):
                return False
            if big.val == sub.val:
                return isSubtreeH(big.left, sub.left) and isSubtreeH(big.right, sub.right)

            return False

        return dfs(root)

        
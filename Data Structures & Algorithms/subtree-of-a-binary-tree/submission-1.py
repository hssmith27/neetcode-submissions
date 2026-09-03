# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node, subRoot):
            if not node:
                return False
            return checkSubtree(node, subRoot) or dfs(node.left, subRoot) or dfs(node.right, subRoot)

        def checkSubtree(main, sub):
            if not main and not sub:
                return True
            if not main and sub or main and not sub:
                return False
            if main.val != sub.val:
                return False
            return checkSubtree(main.left, sub.left) and checkSubtree(main.right, sub.right)
            
        return dfs(root, subRoot)
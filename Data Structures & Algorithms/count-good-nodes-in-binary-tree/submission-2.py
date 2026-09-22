# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, greatest):
            if not node:
                return 0

            left = dfs(node.left, max(greatest, node.val))
            right = dfs(node.right, max(greatest, node.val))

            return left + right + (1 if node.val >= greatest else 0)

        return dfs(root, -101)

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
            good_node = 0
            if node.val >= greatest:
                good_node = 1
            greatest = max(greatest, node.val)
            return good_node + dfs(node.left, greatest) + dfs(node.right, greatest)

        return dfs(root, -101)
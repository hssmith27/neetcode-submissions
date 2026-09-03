# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthH(node, depth):
            if node is None:
                return depth
            return max(maxDepthH(node.left, depth + 1), maxDepthH(node.right, depth + 1))

        return maxDepthH(root, 0)
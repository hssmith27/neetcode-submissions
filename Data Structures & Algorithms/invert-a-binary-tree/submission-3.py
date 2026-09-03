# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invertTreeH(root)
        return root

    def invertTreeH(self, node):
        if not node:
            return
        left = node.left
        node.left = node.right
        node.right = left
        self.invertTreeH(node.left)
        self.invertTreeH(node.right)

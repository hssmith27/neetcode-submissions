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
        if node:
            left = node.left
            right = node.right
            node.right = left
            node.left = right
            self.invertTreeH(node.left)
            self.invertTreeH(node.right)

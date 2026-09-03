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

    def invertTreeH(self, curr):
        if curr is None:
            return
        self.invertTreeH(curr.left)
        self.invertTreeH(curr.right)
        left = curr.left
        right = curr.right
        curr.left = right
        curr.right = left

        
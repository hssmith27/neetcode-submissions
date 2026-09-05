# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def isSameTreeH(one, two):
            if not one and not two:
                return True
            elif not one and two:
                return False
            elif one and not two:
                return False
            elif one.val != two.val:
                return False
            return isSameTreeH(one.left, two.left) and isSameTreeH(one.right, two.right)

        
        return isSameTreeH(p, q)
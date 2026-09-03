# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def helper(root, level):
            if root:
                if level < len(res):
                    res[level].append(root.val)
                else:
                    res.append([root.val])
                helper(root.left, level + 1)
                helper(root.right, level + 1)
            
        helper(root, 0)
        res = [level[-1] for level in res]
        return res
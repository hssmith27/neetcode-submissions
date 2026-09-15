# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(curr, res, height):
            if not curr:
                return
            if height == len(res):
                res.append([curr.val])
            else:
                res[height].append(curr.val)
            dfs(curr.left, res, height + 1)
            dfs(curr.right, res, height + 1)

        dfs(root, res, 0)
        return res

        

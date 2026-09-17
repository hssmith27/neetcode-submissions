# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(cur, res, height):
            if cur is None:
                return
            if height == len(res):
                res.append([cur.val])
            else:
                res[height].append(cur.val)
            dfs(cur.left, res, height + 1)
            dfs(cur.right, res, height + 1)

        dfs(root, res, 0)

        final = []
        for level in res:
            final.append(level[-1])

        return final
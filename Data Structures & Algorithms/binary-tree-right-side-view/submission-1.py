# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node, level, res):
            if node:
                if level >= len(res):
                    res.append([node.val])
                else:
                    res[level].append(node.val)
                dfs(node.left, level + 1, res)
                dfs(node.right, level + 1, res)
            
        dfs(root, 0, res)

        return [level[-1] for level in res]
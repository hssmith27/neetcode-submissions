# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest_paths = defaultdict(int)
        self.diameterH(root, longest_paths)

        def dfs(node):
            if not node:
                return 0
            max_length = 0
            if node.left:
                max_length += longest_paths[node.left] + 1
            if node.right:
                max_length += longest_paths[node.right] + 1
            max_length
            return max(max_length, max(dfs(node.left), dfs(node.right)))

        return dfs(root)

    def diameterH(self, node, longest_paths):
        if not node:
            return 0
        longest_paths[node] = max(self.diameterH(node.left, longest_paths), self.diameterH(node.right, longest_paths))
        return 1 + longest_paths[node]

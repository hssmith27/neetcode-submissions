"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}

        def dfs(cur):
            if cur.val in nodes:
                return nodes[cur.val]
            new = Node(cur.val)
            nodes[cur.val] = new
            new_neighbors = []
            for nei in cur.neighbors:
                new_neighbors.append(dfs(nei))

            new.neighbors = new_neighbors
            return nodes[cur.val]

        dfs(node)

        return nodes[1]
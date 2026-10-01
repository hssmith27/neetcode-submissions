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
        created = {}

        def helper(clonable):
            value = clonable.val
            if value in created:
                return created[value]

            adj = []

            clone = Node(val=value, neighbors=adj)
            created[value] = clone
            
            for nei in clonable.neighbors:
                adj.append(helper(nei))

            
            
            return clone

        return helper(node)
        
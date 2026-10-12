class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        removable = deque()

        for i in range(1, len(adj) + 1):
            if len(adj[i]) == 1:
                removable.append(i)

        while removable:
            removed = removable.popleft()
            for nei in adj[removed]:
                adj[nei].remove(removed)
                if len(adj[nei]) == 1:
                    removable.append(nei)

            adj[removed] = []

        for a, b in reversed(edges):
            if len(adj[a]) == 2 and len(adj[b]) == 2:
                return [a, b]

        return [-1, -1]

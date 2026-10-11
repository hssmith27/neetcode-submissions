class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = defaultdict(list)

        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)

        visited = set()

        def dfs(node, prev):
            if node in visited:
                return True
            
            visited.add(node)
            for nei in adj[node]:
                if nei != prev:
                    dfs(nei, node)

        if dfs(0, -1):
            return False

        return len(visited) == n
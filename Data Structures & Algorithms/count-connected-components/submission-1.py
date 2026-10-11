class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, visited):
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, visited)
        res = 0
        visited = set()

        for i in range(n):
            if i in visited:
                continue
            res += 1
            dfs(i, visited)

        return res

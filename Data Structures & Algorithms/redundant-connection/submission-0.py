class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1

        adj = [[] for _ in range(n)]
        
        def dfs(node, par):
            if visit[node]:
                return True
            visit[node] = True
            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, node):
                    return True
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            visit = [False] * (n)
            if dfs(a, -1):
                return [a, b]
        return []

        
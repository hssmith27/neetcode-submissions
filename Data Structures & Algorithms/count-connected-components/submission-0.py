class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        visited = set()
        total = 0

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for nei in adj_list[node]:
                dfs(nei)

        cur = 0
        while len(visited) != n:
            if cur in visited:
                cur += 1
                continue
            dfs(cur)
            total += 1

        return total
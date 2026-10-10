class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        visited = {}
        outgoing = defaultdict(list)

        for edge in edges:
            source, dest = edge
            outgoing[source].append(dest)
            outgoing[dest].append(source)

        q = deque()
        visited[0] = 1
        for out in outgoing[0]:
            q.append([out, 0])

        while q:
            node, prev = q.popleft()

            if node in visited:
                return False

            visited[node] = 1
            for out in outgoing[node]:
                if out != prev:
                    q.append([out, node])

        return len(visited) == n
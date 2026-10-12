class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            t = time
            visited.add(node)
            for nei, cost in edges[node]:
                heapq.heappush(minHeap, (time + cost, nei))

        return t if len(visited) == n else -1
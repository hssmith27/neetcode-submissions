class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        totals = defaultdict(int)

        for u, v, t in times:
            adj[u].append((v, t))

        for i in range(1, n + 1):
            totals[i] = -1
        totals[k] = 0

        heap = []

        for nei, time in adj[k]:
            heapq.heappush(heap, (time, nei))

        while heap:
            time, nei = heapq.heappop(heap)
            if totals[nei] != -1:
                continue
            totals[nei] = time
            for other, cost in adj[nei]:
                heapq.heappush(heap, (time + cost, other))

        for i in range(1, n + 1):
            if totals[i] == -1:
                return -1

        return max(totals.values())

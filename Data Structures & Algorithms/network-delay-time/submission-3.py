class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        totals = defaultdict(int)

        for i in range(1, n + 1):
            totals[i] = float('inf')
        totals[k] = 0

        for i in range(n - 1):
            for u, v, w in times:
                totals[v] = min(totals[v], totals[u] + w)

        for i in range(n + 1):
            if totals[i] == float('inf'):
                return -1

        return max(totals.values())

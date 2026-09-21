class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1

        for task, count in counts.items():
            heapq.heappush(heap, -count)

        cycles = 0
        pending = deque()
        while heap or pending:
            cycles += 1
            if not heap:
                cycles = pending[0][1]
            else:
                cnt = 1 + heapq.heappop(heap)
                if cnt:
                    pending.append([cnt, cycles + n])
            if pending and pending[0][1] == cycles:
                heapq.heappush(heap, pending.popleft()[0])


        return cycles